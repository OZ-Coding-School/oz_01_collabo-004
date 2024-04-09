from rest_framework import serializers

from .models import Coupon, UserCoupon


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"


class CouponInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        exclude = ["created_at", "modified_at", "id"]


class UserCouponSerializer(serializers.ModelSerializer):
    coupon_info = CouponInfoSerializer(source="coupon", read_only=True)

    class Meta:
        model = UserCoupon
        fields = "__all__"
        read_only_fields = [
            "status",
        ]
