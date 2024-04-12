from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Category
        fields = "__all__"
