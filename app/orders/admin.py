from django.contrib import admin

from config import constants
from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ("sale_price", "total_price", "return_date")
    # 어드민 페이지에서 상세페이지로 볼 정보들
    fieldsets = [
        (
            "주문 상세 정보",
            {
                "fields": [
                    "product",
                    "user",
                    "user_coupon",
                    "status",
                ],
            },
        ),
        (
            "주문 옵션 정보",
            {
                "fields": [
                    "people",
                    "pet_size_small",
                    "pet_size_medium",
                    "pet_size_big",
                ]
            },
        ),
        (
            "출발일 지정",
            {"fields": ["departure_date", "return_date"]},
        ),
        ("가격 정보", {"fields": ["sale_price", "total_price"]}),
    ]
    list_display = [
        "order_id",
        "user",
        "product",
        "used_coupon",
        "departure_date",
        "return_date",
        "origin_price",
        "option_price",
        "sale_price",
        "total_price",
        "status",
        "created_at",
        "modified_at",
    ]

    search_fields = ("product", "user", "user__user_coupon")
    ordering = ("product", "created_at")

    def option_price(self, obj):
        big_size_pet_price = obj.pet_size_big * constants.BIG_SIZE_PET_PRICE
        medium_size_pet_price = obj.pet_size_medium * constants.MEDIUM_SIZE_PET_PRICE
        small_size_pet_price = obj.pet_size_small * constants.SMALL_SIZE_PET_PRICE
        people_price = obj.people * constants.PEOPLE_PRICE
        sum = people_price + big_size_pet_price + medium_size_pet_price + small_size_pet_price
        return sum

    def used_coupon(self, obj):
        if obj.user_coupon is not None:
            return obj.user_coupon
        return None

    def origin_price(self, obj):
        if obj.product.price is not None:
            return obj.product.price
        return None

    def save_model(self, request, obj, form, change):
        if obj.return_date is None:
            obj.return_date = obj.cal_return_date()
        if obj.sale_price is None:
            obj.sale_price = obj.product.discount
            if obj.user_coupon is not None:
                if obj.user_coupon.coupon is not None:
                    obj.sale_price += obj.user_coupon.coupon.sale_price
        if obj.total_price is None:
            obj.total_price = obj.product.price + self.option_price(obj) - obj.sale_price
        super().save_model(request, obj, form, change)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        response = super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)

        new_obj = self.get_object(request, object_id)

        new_obj.return_date = new_obj.cal_return_date()
        new_obj.sale_price = new_obj.product.discount
        if new_obj.user_coupon is not None:
            if new_obj.user_coupon.coupon is not None:
                new_obj.sale_price += new_obj.user_coupon.coupon.sale_price
        new_obj.total_price = new_obj.product.price + self.option_price(new_obj) - new_obj.sale_price
        new_obj.save()

        return response

    def status_set_ordered(self, request, queryset):
        if queryset.count() > 0:
            for obj in queryset:
                obj.stauts = "ORDERED"
                obj.save()

    def status_set_cancel(self, request, queryset):
        if queryset.count() > 0:
            for obj in queryset:
                obj.stauts = "CANCLE"
                obj.save()

    def status_set_paid(self, request, queryset):
        if queryset.count() > 0:
            for obj in queryset:
                obj.stauts = "PAID"
                obj.save()

    status_set_ordered.short_description = "주문 상태로 변경"
    status_set_cancel.short_description = "주문 취소 상태로 변경"
    status_set_paid.short_description = "주문 완료 - 결제 완료 상태로 변경"
    actions = ["status_set_ordered", "status_set_cancel", "status_set_paid"]
