from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import Order
from products.models import Product
# from coupons.models import Coupon, UserCoupon
from .serializers import OrderListSerializer, OrderDetailSerializer
from django.shortcuts import get_object_or_404


class OrderListView(APIView):
    serializer_class = OrderListSerializer

    def check_pet_count(self, data):
        pet_count = data['option_pets']
        sum_selected_size = \
            data['pet_size_big'] + data['pet_size_medium'] + data['pet_size_small']
        return pet_count == sum_selected_size

    def get(self, request):
        orders = Order.objects.filter(user_id=request.user.id, status__ne='CANCEL').all()
        if orders:
            serializer = OrderListSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        order_data = request.data

        if not self.check_pet_count(order_data):
            return Response({'msg': 'plz check pet size count & pet count'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, id=order_data['product'])

        sale_price = 0
        """
        To Do
        주문시 사용한 쿠폰 상태 바꿔주는 로직 작성하기
        """
        # if order_data['coupon']:
        #     used_coupon = get_object_or_404(UserCoupon, user=request.user, coupon_id=order_data['coupon'])
        #     sale_price = used_coupon.sale_price

        total_price = product.price - sale_price

        data = {
            **order_data,
            'status': 'ORDERED',
            'sale_price': sale_price,
            'total_price': total_price
        }

        serializer = OrderListSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
    serializer_class = OrderDetailSerializer

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id, user_id=request.user.id)
        if order.status == 'CANCEL':
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        order = get_object_or_404(Order, id=order_id, user_id=request.user.id)
        if order.status == 'CANCEL':
            return Response(status=status.HTTP_404_NOT_FOUND)
        update_data = request.data
        serializer = OrderDetailSerializer(order, data=update_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id):
        """
        To Do
        주문 취소시 사용한 쿠폰 돌려주는 로직 작성하기
        """
        order = get_object_or_404(Order, id=order_id, user_id=request.user.id)
        if order.status == 'ORDERED' or order.status == 'PAID':
            order.status = 'CANCEL'
            order.save()
            return Response({'msg':'Successfully Canceled'}, status=status.HTTP_200_OK)
        elif order.status == 'CANCEL':
            return Response({'msg':'already cancelled'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'invalid request plz try again'}, status=status.HTTP_400_BAD_REQUEST)
