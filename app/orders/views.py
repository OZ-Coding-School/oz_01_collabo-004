import re

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from coupons.models import Coupon, UserCoupon
from coupons.services import coupon_apply
from products.models import Product

from .models import Order
from .serializers import (
    BankTransferSerializer,
    OrderDetailSerializer,
    OrderListSerializer,
)


def check_pet_count(data):
    pet_count = int(data.get("pet", 0))
    size_big = int(data.get("pet_size_big", 0))
    size_medium = int(data.get("pet_size_medium", 0))
    size_small = int(data.get("pet_size_small", 0))

    # 선택된 사이즈의 합계를 계산
    sum_selected_size = size_big + size_medium + size_small

    return pet_count == sum_selected_size


class OrderListView(APIView):
    serializer_class = OrderListSerializer

    def get(self, request):
        """
        취소된 주문을 제외한 모든 주문을 조회할 수 있음.
        """
        orders = Order.objects.filter(user_id=request.user.id).exclude(status="CANCEL").all()
        if orders:
            serializer = OrderListSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        order_data = request.data

        if not check_pet_count(order_data):
            return Response(
                {"msg": "plz check pet size count & pet count."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        product = Product.objects.filter(id=order_data["product"]).first()
        if product is None:
            return Response(
                {"msg": "plz check product_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        sale_price = 0

        if "user_coupon" in order_data:
            # 유저가 소유한 쿠폰이 맞는지 확인
            used_coupon = get_object_or_404(UserCoupon, user_id=request.user.id, id=order_data["user_coupon"])
            coupon_info = get_object_or_404(Coupon, id=used_coupon.coupon_id)  # 유저가 소유한 쿠폰에 대한 정보를 가져옴
            sale_price = coupon_info.sale_price  # 가져온 정보에서 할인가격을 가져옴

        total_price = product.price - sale_price

        data = {"status": "ORDERED", "sale_price": sale_price, "total_price": total_price, "user": request.user.id}
        for key, value in order_data.items():
            data[key] = value

        serializer = OrderListSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if "user_coupon" in order_data:
            response = coupon_apply(request, order_data["user_coupon"])  # 쿠폰 적용 시도
            if response.status_code != status.HTTP_200_OK:  # 쿠폰 적용 실패시 주문이 취소됨
                return Response({"msg": response.data["msg"]}, response.status_code)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


def is_uuid4(value):
    pattern = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$", re.IGNORECASE)
    return bool(pattern.match(value))


class OrderDetailView(APIView):
    serializer_class = OrderDetailSerializer

    def get(self, request, order_id):
        if not is_uuid4(order_id):
            return Response({"msg": "Invalid order_id"}, status=status.HTTP_400_BAD_REQUEST)
        order = get_object_or_404(Order, order_id=order_id, user_id=request.user.id)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        order = get_object_or_404(Order, order_id=order_id, user_id=request.user.id)
        # 취소된 주문은 수정이 불가함을 알림
        if order.status == "CANCEL":
            return Response({"msg": "already canceled order."}, status=status.HTTP_400_BAD_REQUEST)
        # 이미 결제된 주문은 수정이 불가함을 알림
        if order.status == "PAID":
            return Response({"msg": "already paid order."}, status=status.HTTP_400_BAD_REQUEST)
        update_data = request.data
        serializer = OrderDetailSerializer(order, data=update_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id):
        order = get_object_or_404(Order, order_id=order_id, user_id=request.user.id)
        if order.status == "ORDERED" or order.status == "PAID":
            order.status = "CANCEL"  # 주문 취소상태 설정
            if order.user_coupon_id is not None:  # 만약 주문시 사용한 쿠폰이 있으면
                order.user_coupon.status = True  # 쿠폰을 사용가능 상태로 만들어줌
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
