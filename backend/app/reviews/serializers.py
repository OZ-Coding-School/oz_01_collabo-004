from rest_framework.serializers import Serializer, ModelSerializer
from .models import ProductReview


class ProductReviewListSerializer(ModelSerializer):
    class Meta:
        model = ProductReview
        fields = "__all__"
        depth = 1


class ProductReviewSerializer(ModelSerializer):
    class Meta:
        model = ProductReview
        fields = "__all__"
