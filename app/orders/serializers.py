from rest_framework import serializers

from coupons.serializers import UserCouponSerializer
from products.models import Product
from products.serializers import ProductInfoSerializer

from .models import Order, Payment


class OrderListSerializer(serializers.ModelSerializer):  # type: ignore
    product_info = ProductInfoSerializer(source="product", read_only=True)
    product = serializers.IntegerField(write_only=True)
    user_coupon_id = serializers.IntegerField(write_only=True)
    coupon = UserCouponSerializer(source="user_coupon", read_only=True)

    class Meta:
        model = Order
        exclude = ("user",)
        read_only_fields = ["order_id", "status", "sale_price", "total_price", "return_date"]


class OrderDetailSerializer(serializers.ModelSerializer):  # type: ignore
    product = ProductInfoSerializer(read_only=True)
    user_coupon = UserCouponSerializer(read_only=True)
    # payment_info = PaymentInfoSerialzier(read_only=True)

    class Meta:
        model = Order
        exclude = ("user",)
        read_only_fields = ["user", "order_id", "sale_price", "total_price", "status"]
        depth = 1


class BankTransferSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Payment
        fields = "__all__"
