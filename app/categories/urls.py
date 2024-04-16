from django.urls import path

from .views import (
    CategoryDetailView,
    CategoryListView,
    UserCategoryDetailView,
    UserCategoryListView,
    UserCategorySurveyView,
)

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path(
        "categories/<int:category_pk>/",
        CategoryDetailView.as_view(),
        name="category-detail",
    ),
    path("categories/user-surver/", UserCategorySurveyView.as_view(), name="user-survey"),
    path("categories/user-categories/<int:category_id>", UserCategoryListView.as_view(), name="user-categories"),
    path("categories/user-detail/<int:category_id>", UserCategoryDetailView.as_view(), name="user-detail"),
]
