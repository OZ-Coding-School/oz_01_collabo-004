from django.urls import path

from . import views

urlpatterns = [
    path("", views.MyReviewListView.as_view(), name="product-review-list"),
    path(
        "mypage/<int:review_id>/",
        views.MyReviewDetailView.as_view(),
        name="product-review-detail",
    ),
    path("<int:review_id>/", views.ReviewDetailView.as_view(), name="review-detail"),
    # path("upload/imagefile/", views.ProductReviewImageUploadView.as_view(), name="review-image-upload"),
    path("product/<int:product_id>/", views.ProductReviewListView.as_view(), name="product-page-reviews"),
]
