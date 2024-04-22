from django.contrib import admin

from common.utils import S3ImgUploader

from .models import ProductReview


@admin.register(ProductReview)
class ReviewAdmin(admin.ModelAdmin):
    # 어드민 페이지에서 상세페이지로 볼 리뷰 정보들
    fieldsets = (("리뷰 정보", {"fields": ("title", "image_url", "content", "status", "user", "product")}),)

    # 리뷰를 만들때 보이는 화면
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("title", "image_url", "content", "status", "user", "product"),
            },
        ),
    )

    # 표에서 보이는 정보
    list_display = ("title", "content", "status", "user", "product")
    search_fields = ("title", "content")
    ordering = ("id",)

    # 기본 actions에 세팅된 delete_selected 제거
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def save_model(self, request, obj, form, change):
        obj.save()

    def delete_model(self, request, obj):
        image_uploader = S3ImgUploader()
        if obj.image_url:
            image_uploader.delete_img_file(str(obj.image_url))

        return super().delete_model(request, obj)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        """
        ModelAdmin.change_view를 오버라이드해서 업데이트 시 기존의 이미지는 삭제하고 새로운 이미지를 S3에 저장
        """
        change_review = self.get_object(request, object_id)
        if change_review is not None:
            if change_review.image_url is not None:
                image_uploader = S3ImgUploader()
                image_uploader.delete_img_file(str(change_review.image_url))
            return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)
        return None

    def delete_selected_model(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)

    def activate_reviews(self, request, queryset):
        if queryset.count() > 0:
            for obj in queryset:
                obj.status = True
                obj.save()

    def disabled_reviews(self, request, queryset):
        if queryset.count() > 0:
            for obj in queryset:
                obj.status = False
                obj.save()

    def reset_view_count(self, request, queryset):
        if queryset.count() > 0:
            for obj in queryset:
                obj.view_count = 0
                obj.save()

    # actions 수정
    delete_selected_model.short_description = "Delete selected reviews"
    activate_reviews.short_description = "Activate reviews"
    disabled_reviews.short_description = "Disabled reviews"
    reset_view_count.short_description = "Reset view count"
    actions = ["delete_selected_model", "activate_reviews", "disabled_reviews", "reset_view_count"]
