from rest_framework import serializers

from .models import Category, CategoryProductConnector, CategoryUserConnector


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserConnectorSerializer(serializers.ModelSerializer):
    category_name = CategorySerializer(read_only=True)

    class Meta:
        model = CategoryUserConnector
        fields = "__all__"


class ProductConnectorSerializer(serializers.ModelSerializer):
    category_name = CategorySerializer(read_only=True)

    class Meta:
        model = CategoryProductConnector
        fields = "__all__"
