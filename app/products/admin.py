from django.contrib import admin

from common.utils import S3ImgUploader

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # 어드민 페이지에서 상세페이지로 볼 상품 정보들
    fieldsets = (
        ("Product Info", {"fields": ("name", "product_img", "description_img", "description_text", "travel_period")}),
        ("Price and Sale", {"fields": ("price", "discount")}),
        ("Status and View Count", {"fields": ("status", "view_count")}),
    )

    # 표에서 보이는 정보
    list_display = ("name", "description_text", "price", "discount", "travel_period", "view_count", "status")
    search_fields = ("price", "name", "description_text")
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
        if obj.product_img:
            image_uploader.delete_img_file(str(obj.product_img))
        if obj.description_img:
            image_uploader.delete_img_file(str(obj.description_img))

        super().delete_model(request, obj)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        """
        ModelAdmin.change_view를 오버라이드해서 업데이트 시 기존의 이미지는 삭제하고 새로운 이미지를 S3에 저장
        """
        prev_product = self.get_object(request, object_id)

        response = super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)

        updated_product = self.get_object(request, object_id)
        if updated_product.product_img != prev_product.product_img:
            if updated_product.product_img:
                image_uploader = S3ImgUploader()
                image_uploader.delete_img_file(str(prev_product.product_img))
        if updated_product.description_img != prev_product.description_img:
            if updated_product.description_img:
                image_uploader = S3ImgUploader()
                image_uploader.delete_img_file(str(prev_product.product_img))
        return response

    def delete_selected_model(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)

    def start_sales_products(self, request, queryset):
        if queryset.count() > 0:
            for obj in queryset:
                obj.status = True
                obj.save()

    def stop_sales_products(self, request, queryset):
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
    delete_selected_model.short_description = "Delete selected products"
    start_sales_products.short_description = "Start sales products"
    stop_sales_products.short_description = "Stop sales products"
    reset_view_count.short_description = "Reset view count"
    actions = ["delete_selected_model", "start_sales_products", "stop_sales_products", "reset_view_count"]
