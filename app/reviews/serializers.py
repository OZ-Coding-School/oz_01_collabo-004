from rest_framework import serializers

from products.serializers import ProductInfoSerializer

from .models import ProductReview


class MyReviewListSerializer(serializers.ModelSerializer):  # type: ignore
    product_info = ProductInfoSerializer(source="product", read_only=True)

    class Meta:
        model = ProductReview
        exclude = ("user",)
        read_only_fields = ("status",)


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        exclude = ("user",)
        read_only_fields = ("status", "created_at", "modified_at")


class ProductReviewDetailSerializer(serializers.ModelSerializer):  # type: ignore
    product = ProductInfoSerializer(read_only=True)

    class Meta:
        model = ProductReview
        exclude = ("user",)
        read_only_fields = ["status", "created_at", "modified_at"]


class ProductReviewListSerializer(serializers.ModelSerializer):
    writer = serializers.CharField(source="user.nickname", read_only=True)
    profile_image = serializers.ImageField(source="user.profile_image", read_only=True)

    class Meta:
        model = ProductReview
        exclude = ("user",)
        read_only_fields = ["created_at", "modified_at"]
