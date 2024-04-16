from rest_framework import serializers

from products.serializers import ProductInfoSerializer, ProductSerializer

from .models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):  # type: ignore
    product = ProductInfoSerializer(read_only=True)

    class Meta:
        model = Wishlist
        exclude = (
            "created_at",
            "modified_at",
        )
        depth = 1


class WishlistSerializer(serializers.ModelSerializer):  # type: ignore
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Wishlist
        exclude = ("created_at", "modified_at", "user")
        depth = 1


class CreateWishlistSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Wishlist
        exclude = ("created_at", "modified_at", "user")
        read_only_fields = ("status",)
