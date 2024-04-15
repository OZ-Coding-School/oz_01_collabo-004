from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "주문 내역 정보",
            {
                "fields": ["user", "status", "product", "option"],
            },
        ),
    ]
    list_display = ["id", "user", "status", "product", "total_price"]
