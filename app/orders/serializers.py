from rest_framework import serializers

from products.models import Product
from products.serializers import ProductInfoSerializer

from .models import Order, Payment


class OrderListSerializer(serializers.ModelSerializer):
    product_info = ProductInfoSerializer(source="product", read_only=True)
    # payment_info = PaymentInfoSerialzier(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["order_id"]


class OrderDetailSerializer(serializers.ModelSerializer):
    product_info = ProductInfoSerializer(source="product", read_only=True)
    # payment_info = PaymentInfoSerialzier(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["user", "order_id", "sale_price", "total_price", "status"]


class BankTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
