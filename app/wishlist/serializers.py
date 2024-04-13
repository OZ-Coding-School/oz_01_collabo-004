from rest_framework import serializers

from products.serializers import ProductSerializer

from .models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):  # type: ignore
    product = ProductSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # type: ignore

    class Meta:
        model = Wishlist
        exclude = (
            "created_at",
            "modified_at",
        )
        depth = 1


class CreateWishlistSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Wishlist
        exclude = (
            "id",
            "created_at",
            "modified_at",
        )
