from rest_framework.urls import path

from . import views

urlpatterns = [
    path("", views.ProductReviewListView.as_view(), name="product-review-list"),
    path(
        "<int:product_id>/",
        views.ProductReviewDetailView.as_view(),
        name="product-review-detail",
    ),
]
