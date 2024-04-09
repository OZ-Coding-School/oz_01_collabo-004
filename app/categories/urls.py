from django.urls import path

from .views import CategoryDetailView, CategoryListView, UserCategorySurveyView

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path(
        "categories/<int:category_pk>/",
        CategoryDetailView.as_view(),
        name="category-detail",
    ),
    path("categories/user-surver/", UserCategorySurveyView.as_view(), name="user-survey"),
]
