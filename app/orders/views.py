import re
from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from coupons.services import change_coupon_status
from orders.utils import cal_option_price
from products.models import Product

from .models import Order
from .serializers import (
    BankTransferSerializer,
    OrderDetailSerializer,
    OrderListSerializer,
)


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

        serializer = OrderListSerializer(data=order_data)
        # 요청을 통해 들어온 데이터가 유효한지 판단
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # 상품의 아이디 값이 유효한지 검증하면서 필요한 데이터 가져오기
        product = Product.objects.filter(id=order_data["product"]).first()
        if product is None:
            return Response(
                {"msg": "plz check product_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 할인가는 기본 상품의 할인가
        sale_price = product.discount

        # 만약 쿠폰을 사용했다면 쿠폰의 할인가를 추가로 적용
        if order_data.get("user_coupon_id"):
            try:
                # 쿠폰 적용 시도 후 성공하면 할인가격을 가져옴
                sale_price += change_coupon_status(user_coupon_id=order_data["user_coupon_id"], new_status=False)
            except ValidationError as e:
                return Response({"msg": e.message}, status=status.HTTP_400_BAD_REQUEST)

        total_price = product.price + cal_option_price(request.data) - sale_price

        serializer.save(
            product=product,
            status="ORDERED",
            sale_price=sale_price,
            total_price=total_price,
            user=request.user,
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


def is_uuid4(value: str) -> bool:
    pattern = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$", re.IGNORECASE)
    return bool(pattern.match(value))


class OrderDetailView(APIView):
    serializer_class = OrderDetailSerializer

    def get(self, request: Request, order_id: str) -> Response:
        """
        로그인 한 유저가 자신의 주문내역 중 하나를 상세히 볼 수 있도록 데이터를 내려주는 get 메서드
        """
        if not is_uuid4(order_id):
            return Response({"msg": "Invalid order_id"}, status=status.HTTP_400_BAD_REQUEST)
        order = get_object_or_404(Order, order_id=order_id, user_id=request.user.id)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, order_id: str) -> Response:
        """
        로그인한 유저가 자신의 주문내역 중에서 아직 결제나 취소가 되지않은 주문에 한해서 옵션, 쿠폰 등을 수정할 수 있는 메서드
        """
        order = get_object_or_404(Order, order_id=order_id, user_id=request.user.id)

        # 취소된 주문은 수정이 불가함을 알림
        if order.status == "CANCEL":
            return Response({"msg": "already canceled order."}, status=status.HTTP_400_BAD_REQUEST)
        # 이미 결제된 주문은 수정이 불가함을 알림
        if order.status == "PAID":
            return Response({"msg": "already paid order."}, status=status.HTTP_400_BAD_REQUEST)

        update_data = request.data.copy()

        # update_data에 대한 유효성 검증
        serializer = OrderDetailSerializer(order, data=update_data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        sale_price = order.sale_price
        # 주문 수정하기에서 쿠폰을 변경할 시 기존에 주문에 적용됐던 쿠폰은 되돌리고, 새로 적용할 쿠폰을 적용함
        if update_data.get("user_coupon_id"):
            try:
                if order.user_coupon:
                    prev_sale_price = change_coupon_status(order.user_coupon.id, True)  # type: ignore
                    sale_price -= prev_sale_price  # 이전에 적용된 쿠폰 할인 가격을 되돌림
                new_sale_price = change_coupon_status(update_data["user_coupon_id"], False)
                sale_price += new_sale_price  # 새롭게 적용할 쿠폰의 할인 가격을 적용
            except ValueError as e:
                return Response({"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        total_price = order.product.price + cal_option_price(request.data) - sale_price  # type: ignore
        serializer.save(sale_price=sale_price, total_price=total_price)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, order_id: str) -> Response:
        """
        주문 취소 요청시 주문의 status를 cancel로 변환해주는 메서드,,
        """
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
