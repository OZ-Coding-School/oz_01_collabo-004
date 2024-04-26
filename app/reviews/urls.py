from django.urls import path

from . import views

urlpatterns = [
    path("", views.MyReviewListView.as_view(), name="product-review-list"),
    path(
        "<int:review_id>/",
        views.ProductReviewDetailView.as_view(),
        name="product-review-detail",
    ),
    # path("upload/imagefile/", views.ProductReviewImageUploadView.as_view(), name="review-image-upload"),
    path("product/<int:product_id>/", views.ProductReviewListView.as_view(), name="product-page-reviews"),
    path("<int:review_id>/add/view_count/", views.AddReviewViewCount.as_view(), name="add-review-view-count"),
]
