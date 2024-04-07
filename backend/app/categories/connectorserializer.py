from rest_framework import serializers

from .models import CategoryUserConnector


class ConnectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryUserConnector
        fields = "__all__"  # 모든 필드를 포함합니다.
