from .models import Wishlist
from rest_framework import serializers
from products.serializers import ProductSerializer

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Wishlist
        exclude = ('id', 'created_at', 'modified_at',)
        depth = 1

class CreateWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        exclude = ('id', 'created_at', 'modified_at',)