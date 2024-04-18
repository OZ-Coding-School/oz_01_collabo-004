from django.contrib import admin

from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    # 어드민 페이지에서 상세페이지로 볼 위시리스트 정보들
    fieldsets = (("위시리스트 정보", {"fields": ("user", "product", "status")}),)

    # 위시리스트를 만들때 보이는 화면
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("user", "product", "status"),
            },
        ),
    )

    # 표에서 보이는 정보
    list_display = ("user", "product", "status")
    search_fields = ("user__username", "product__name")
    ordering = ("product",)

    def activate_wishlist(self, request, queryset):
        if queryset.count() > 0:
            for obj in queryset:
                obj.status = True
                obj.save()

    def disabled_wishlist(self, request, queryset):
        if queryset.count() > 0:
            for obj in queryset:
                obj.status = False
                obj.save()

    activate_wishlist.short_description = "Activate wishlist"
    disabled_wishlist.short_description = "Disable wishlist"
    actions = ["activate_wishlist", "disabled_wishlist"]
