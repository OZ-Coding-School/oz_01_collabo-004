import re
from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from coupons.models import UserCoupon
from coupons.services import change_coupon_status
from products.models import Product

from .models import Order
from .serializers import (
    BankTransferSerializer,
    OrderDetailSerializer,
    OrderListSerializer,
)


def check_pet_count(data) -> bool:  # type: ignore
    pet_count = int(data.get("pet", 0))
    size_big = int(data.get("pet_size_big", 0))
    size_medium = int(data.get("pet_size_medium", 0))
    size_small = int(data.get("pet_size_small", 0))

    # 선택된 사이즈의 합계를 계산
    sum_selected_size = size_big + size_medium + size_small

    return pet_count == sum_selected_size


class OrderListView(APIView):
    serializer_class = OrderListSerializer

    def get(self, request: Request) -> Response:
        """
        취소된 주문을 제외한 모든 주문을 조회할 수 있음.
        """
        orders = Order.objects.filter(user_id=request.user.id).exclude(status="CANCEL").order_by("created_at")  # type: ignore
        if orders:
            serializer = OrderListSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request: Request) -> Response:
        """
        유저가 주문을 요청하면 각각의 데이터의 유효성을 검증하고 주문을 생성해주는 post 메서드
        """

        order_data = request.data

        serializer = OrderListSerializer(data=order_data, partial=True)
        # 요청을 통해 들어온 데이터가 유효한지 판단
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # 상품의 아이디 값이 유효한지 판단
        product = Product.objects.filter(id=order_data["product"]).first()
        if product is None:
            return Response(
                {"msg": "plz check product_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 상품의 옵션 중 반려동물의 수 와 사이즈 합계가 맞는지 검증
        if not check_pet_count(order_data):
            return Response(
                {"msg": "plz check pet size count & pet count."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # timedelta를 사용하여 반환 날짜 계산
        departure_date = datetime.strptime(order_data["departure_date"], "%Y-%m-%d")
        return_date = departure_date + timedelta(days=product.travel_period)

        # 할인가는 기본 0원
        sale_price = 0

        # 만약 쿠폰을 사용했다면 쿠폰의 할인가를 적용
        if "user_coupon_id" in order_data:
            try:
                # 쿠폰 적용 시도 후 성공하면 할인가격을 가져옴
                sale_price = change_coupon_status(user_coupon_id=order_data["user_coupon_id"], new_status=False)
            except ValidationError as e:
                return Response({"msg": e.message}, status=status.HTTP_400_BAD_REQUEST)

        total_price = product.price - sale_price

        serializer.save(
            product=product,
            status="ORDERED",
            sale_price=sale_price,
            total_price=total_price,
            return_date=return_date.date(),
            user=request.user,
        )

        serializer.instance.return_date = serializer.instance.cal_return_date()  # type: ignore
        serializer.instance.save()  # type: ignore

        return Response(serializer.data, status=status.HTTP_201_CREATED)


def is_uuid4(value: str) -> bool:
    pattern = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$", re.IGNORECASE)
    return bool(pattern.match(value))


class OrderDetailView(APIView):
    serializer_class = OrderDetailSerializer

    def get(self, request: Request, order_id: str) -> Response:
        if not is_uuid4(order_id):
            return Response({"msg": "Invalid order_id"}, status=status.HTTP_400_BAD_REQUEST)
        order = get_object_or_404(Order, order_id=order_id, user_id=request.user.id)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, order_id: str) -> Response:
        order = get_object_or_404(Order, order_id=order_id, user_id=request.user.id)

        # 취소된 주문은 수정이 불가함을 알림
        if order.status == "CANCEL":
            return Response({"msg": "already canceled order."}, status=status.HTTP_400_BAD_REQUEST)
        # 이미 결제된 주문은 수정이 불가함을 알림
        if order.status == "PAID":
            return Response({"msg": "already paid order."}, status=status.HTTP_400_BAD_REQUEST)

        update_data = request.data.copy()

        # 주문 수정 데이터에 출발일 변경을 원하면 출발일과 product의 trevel_date를 이용해서 도착일을 계산
        if "departure_date" in update_data:
            departure_date = datetime.strptime(update_data["departure_date"], "%Y-%m-%d")
            return_date = departure_date + timedelta(days=order.product.travel_period)  # type: ignore
            update_data["return_date"] = return_date.date()

        # request.data에 대한 유효성 검증
        serializer = OrderDetailSerializer(order, data=update_data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # 주문 수정하기에서 쿠폰을 변경할 시 기존에 주문에 적용됐던 쿠폰은 되돌리고, 새로 적용할 쿠폰을 적용함
        if "user_coupon_id" in update_data:
            try:
                change_coupon_status(order.user_coupon.id, True)  # type: ignore
                change_coupon_status(update_data["user_coupon_id"], False)
            except ValueError as e:
                return Response({"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, order_id: str) -> Response:
        order = get_object_or_404(Order, order_id=order_id, user_id=request.user.id)
        if order.status == "ORDERED" or order.status == "PAID":
            order.status = "CANCEL"  # 주문 취소상태 설정
            if order.user_coupon_id is not None:  # 만약 주문시 사용한 쿠폰이 있으면
                # 쿠폰을 사용가능 상태로 만들어줌
                order.user_coupon.status = True  # type: ignore
            order.save()
            return Response({"msg": "Successfully Canceled"}, status=status.HTTP_200_OK)
        elif order.status == "CANCEL":
            return Response({"msg": "already cancelled"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"msg": "invalid request plz try again"}, status=status.HTTP_400_BAD_REQUEST)


# class TossPaymentView(APIView):
#     """
#     토스페이 결제처리를 담당할 View
#     """
#     serializer_class = []
#
#     def get(self, request, order_id):
#         order = get_object_or_404(Order, id=order_id, user_id=request.user.id)
#         if order.status == "PAID":
#             return Response({"msg": "already paid order."}, status=status.HTTP_400_BAD_REQUEST)
#         elif order.status == "CANCEL":
#             return Response({"msg": "already cancelled order."}, status=status.HTTP_400_BAD_REQUEST)
#         data = {
#             "order": order_id,
#             "status": "PENDING",
#             "amount": order.total_price,
#             "payment_method": "무통장 입금"
#         }
#         serializer = BankTransferSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def post(self, request, order_id):
#         """
#         결제 처리를 담당할 부분
#         """
#         order = get_object_or_404(Order, id=order_id, user_id=request.user.id)
