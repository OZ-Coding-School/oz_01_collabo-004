from django.contrib import admin
from django.urls import path
from products.views import ProductList, ProductDetail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/products/", ProductList.as_view(), name="product-list-create"),
    path("api/v1/products/<int:pk>/", ProductDetail.as_view(), name="product-detail"),
]
