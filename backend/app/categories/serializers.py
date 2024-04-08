from products.models import Product
from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, required=False)

    class Meta:
        model = Category
        fields = "__all__"
