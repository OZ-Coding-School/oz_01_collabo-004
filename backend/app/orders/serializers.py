from rest_framework import serializers

from products.models import Product
from products.serializers import ProductInfoSerializer

from .models import Order


class OrderListSerializer(serializers.ModelSerializer):
    product_info = ProductInfoSerializer(read_only=True, required=False)
    # payment_info = PaymentInfoSerialzier(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    product_info = ProductInfoSerializer(read_only=True)
    # payment_info = PaymentInfoSerialzier(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["payment_method", "sale_price", "total_price", "status"]
