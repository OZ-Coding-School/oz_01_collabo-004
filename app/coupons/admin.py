from django.contrib import admin

from .models import Coupon, UserCoupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    # 어드민 페이지에서 상세페이지로 볼 정보들
    fieldsets = (
        (
            "쿠폰 정보",
            {
                "fields": (
                    "id",
                    "type",
                    "content",
                    "sale_price",
                    "duration",
                )
            },
        ),
    )

    # 쿠폰을 만들때 보이는 화면
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "type",
                    "content",
                    "sale_price",
                    "duration",
                ),
            },
        ),
    )

    # 표에서 보이는 정보
    list_display = (
        "id",
        "type",
        "sale_price",
        "duration",
    )
    search_fields = ("type", "content", "sale_price")
    ordering = ("id",)


@admin.register(UserCoupon)
class UserCouponAdmin(admin.ModelAdmin):
    def coupon_type(self, obj):
        return obj.coupon.type

    def coupon_sale_price(self, obj):
        return obj.coupon.sale_price

    def coupon_duration(self, obj):
        return obj.coupon.duration

    # 어드민 페이지에서 상세페이지로 볼 정보들
    fieldsets = (
        (
            "쿠폰 정보",
            {"fields": ("user", "coupon", "expired_at")},
        ),
    )

    # 유저쿠폰을 만들때 보이는 화면
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "coupon_id",
                    "user_id",
                    "expired_at",
                ),
            },
        ),
    )

    # 표에서 보이는 정보
    list_display = (
        "id",
        "coupon_id",
        "user_id",
        "coupon_type",
        "coupon_sale_price",
        "coupon_duration",
        "expired_at",
    )
    search_fields = ("user_id", "coupon_id", "expired_at")
    ordering = ("id",)
