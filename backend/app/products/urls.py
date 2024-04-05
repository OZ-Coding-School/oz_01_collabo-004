from django.contrib import admin
from django.urls import path

from products.views import (GetProductByCategoryView, ProductDetailView,
                            ProductListView, ProductSearchView)

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list-create"),
    path("<int:product_id>/", ProductDetailView.as_view(), name="product-detail"),
    path("search/", ProductSearchView.as_view(), name="product-search"),
]
