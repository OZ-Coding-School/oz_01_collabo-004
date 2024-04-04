from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # 어드민 페이지에서 상세페이지로 볼 정보들
    fieldsets = (
        (
            "유저 정보",
            {
                "fields": (
                    "user_id",
                    "password",
                    "name",
                    "email",
                    "phone",
                )
            },
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    # 유저를 만들때 보이는 화면
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("user_id", "password", "password_check", "name", "email", "phone"),
            },
        ),
    )

    # 표에서 보이는 정보
    list_display = ("id", "user_id", "name", "email", "phone", "is_active", "is_staff", "is_superuser", "last_login")
    search_fields = ("email", "name", "user_id", "phone")
    ordering = ("id",)
