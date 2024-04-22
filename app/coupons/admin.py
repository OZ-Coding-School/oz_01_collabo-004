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
                    "type",
                    "content",
                    "sale_price",
                    "duration",
                )
            },
        ),
    )

    # 표에서 보이는 정보
    list_display = (
        "id",
        "content",
        "type",
        "sale_price",
        "duration",
    )

    search_fields = ("type", "content", "sale_price")
    ordering = ("id",)


@admin.register(UserCoupon)
class UserCouponAdmin(admin.ModelAdmin):
    # 어드민 페이지에서 상세페이지로 볼 정보들
    fieldsets = (
        (
            "쿠폰 정보",
            {"fields": ("user", "coupon")},
        ),
    )

    # 표에서 보이는 정보
    list_display = (
        "id",
        "user",
        "coupon",
        "coupon_type",
        "coupon_sale_price",
        "coupon_duration",
        "status",
        "expired_at",
    )
    search_fields = ("user", "coupon", "expired_at")
    ordering = ("coupon",)

    def coupon_type(self, obj):
        return obj.coupon.type

    def coupon_sale_price(self, obj):
        return obj.coupon.sale_price

    def coupon_duration(self, obj):
        return obj.coupon.duration

    def save_model(self, request, obj, form, change):
        if obj.expired_at is None:
            obj.expired_at = obj.get_expire_date()
        return super().save_model(request, obj, form, change)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        """
        유저 쿠폰이 참조하는 쿠폰이 변경될 경우 expired_at도 업데이트 해준다.
        만약 업데이트 하기 전 유저쿠폰이 참조하는 쿠폰과 업데이트 후 유저쿠폰이 참조하는 쿠폰이 달라진다면
        유저 쿠폰의 만료기한을 참조하는 쿠폰의 기간을 참조해서 업데이트 한다.
        """
        prev = self.get_object(request, object_id)

        response = super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)

        new = self.get_object(request, object_id)

        if prev.coupon != new.coupon:
            new.expired_at = new.get_expire_date()
            new.save()

        return response

    def activate_coupon(self, request, queryset):
        if queryset.count() > 0:
            for obj in queryset:
                obj.status = True
                obj.save()

    def not_available_coupon(self, request, queryset):
        if queryset.count() > 0:
            for obj in queryset:
                obj.status = False
                obj.save()

    activate_coupon.short_description = "쿠폰 활성화 하기"
    not_available_coupon.short_description = "쿠폰 비활성화 하기"
    actions = ["activate_coupon", "not_available_coupon"]
