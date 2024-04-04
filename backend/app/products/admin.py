from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # 어드민 페이지에서 상세페이지로 볼 상품 정보들
    fieldsets = (
        (
            "상품 정보",
            {
                "fields": (
                    "name",
                    # 'product_img',
                    # 'description_img',
                    # 'description_text',
                    "price",
                    "sale",
                    "status",
                    "view_count",
                )
            },
        ),
    )

    # 상품을 만들때 보이는 화면
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    # 'product_img',
                    # 'description_img',
                    # 'description_text',
                    "price",
                    "sale",
                    "status",
                    "view_count",
                ),
            },
        ),
    )

    # 표에서 보이는 정보
    list_display = ("name", "description_text", "price", "sale", "status", "view_count")
    search_fields = ("price", "name", "description_text")
    ordering = ("id",)
