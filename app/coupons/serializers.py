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


class UserCouponSerializer(serializers.ModelSerializer):  # type: ignore
    coupon_info = CouponInfoSerializer(source="coupon", read_only=True)
    coupon = serializers.IntegerField(write_only=True)

    class Meta:
        model = UserCoupon
        exclude = ["created_at", "modified_at", "user"]
        read_only_fields = [
            "status",
        ]
