from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = (
            "created_at",
            "modified_at",
        )


class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "product_img", "price", "sale", "status")
