from django.urls import path

from . import views

urlpatterns = [
    path("", views.WishlistView.as_view(), name="wishlist"),
    path("<int:wishlist_id>/", views.WishlistDetailView.as_view(), name="wishlist_detail"),
]
