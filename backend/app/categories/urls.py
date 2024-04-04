from django.urls import path

from .views import CategoryDetailView, CategoryListView

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path(
        "categories/<int:category_pk>/",
        CategoryDetailView.as_view(),
        name="category-detail",
    ),
]
