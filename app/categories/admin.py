from django.contrib import admin

from .models import Category, CategoryProductConnector, CategoryUserConnector


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)
    ordering = ("id",)

    class CategoryProductConnectorInline(admin.StackedInline):
        model = CategoryProductConnector

    inlines = [CategoryProductConnectorInline]


@admin.register(CategoryUserConnector)
class CategoryUserConnectorAdmin(admin.ModelAdmin):
    list_display = ("user", "category")
    list_filter = ("category", "user")
    list_display_links = ("user",)
    search_fields = ("user", "category")
    ordering = ("id",)


@admin.register(CategoryProductConnector)
class CategoryProductConnectorAdmin(admin.ModelAdmin):
    list_display = ("product", "category")
    list_filter = ("category", "product")
    list_display_links = ("product",)
    search_fields = ("product", "category")
    ordering = ("id",)
