from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from common.utils import S3ImgUploader

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
        ("프로필 이미지", {"fields": ("profile_image",)}),
        ("권한 정보", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    # 유저를 만들때 보이는 화면
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "user_id",
                    "password1",
                    "password2",
                    "profile_image",
                    "name",
                    "email",
                    "phone",
                ),
            },
        ),
    )

    # 표에서 보이는 정보
    list_display = (
        "id",
        "user_id",
        "name",
        "email",
        "phone",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
    )
    search_fields = ("email", "name", "user_id", "phone")
    ordering = ("id",)

    def save_model(self, request, obj, form, change):
        obj.save()

    def delete_model(self, request, obj):
        image_uploader = S3ImgUploader()
        if obj.profile_image:
            image_uploader.delete_img_file(str(obj.profile_image))

        return super().delete_model(request, obj)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        """
        ModelAdmin.change_view를 오버라이드해서 업데이트 시 기존의 이미지는 삭제하고 새로운 이미지를 S3에 저장
        """
        prev_user = self.get_object(request, object_id)

        response = super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)

        new_user = self.get_object(request, object_id)
        if prev_user.profile_image is not None:
            if prev_user.profile_image != new_user.profile_image:
                image_uploader = S3ImgUploader()
                image_uploader.delete_img_file(str(prev_user.profile_image))
        return response

    # 기본 actions에 세팅된 delete_selected 제거
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def delete_selected_user(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)

    def activate_user(self, request, queryset):
        if queryset.count() > 0:
            for obj in queryset:
                obj.is_active = True
                obj.save()

    def deactivate_user(self, request, queryset):
        if queryset.count() > 0:
            for obj in queryset:
                obj.is_active = False
                obj.save()

    activate_user.short_description = "유저 활성화"
    deactivate_user.short_description = "유저 비활성화"
    delete_selected_user.short_description = "선택된 유저 삭제"
    actions = ["delete_selected_user", "activate_user", "deactivate_user"]
