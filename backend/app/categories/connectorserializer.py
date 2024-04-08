from rest_framework import serializers

from .models import CategoryUserConnector
from .serializers import CategorySerializer


class ConnectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryUserConnector
        fields = "__all__"  # 모든 필드를 포함합니다.


# class ConnectorDetailSerializer(serializers.ModelSerializer):
#     categories = ConnectorSerializer(many=True)
#     class Meta:
#         model = CategoryUserConnector
#         fields = "id", 'user', 'categories'
#
#     def get_categories(self, obj):
#         category_id = obj.category.id
#         category = CategoryUserConnector.objects.get(id=category_id)
#         serializers = ConnectorSerializer(category, many=True)
#         return serializers.data
# 카테고리 아이디에 해당하는 정보를 가져올수 있도록


class ConnectorDetailSerializer(serializers.ModelSerializer):
    category_info = CategorySerializer(read_only=True)

    class Meta:
        model = CategoryUserConnector
        fields = "__all__"  # 모든 필드를 포함합니다.
