from rest_framework.urls import path

from . import views

urlpatterns = [
    path("mycoupon/", views.UserCouponListView.as_view(), name="user-coupon-list"),
    path(
        "mycoupon/used",
        views.UsedUserCouponListView.as_view(),
        name="used-user-coupons",
    ),
    path(
        "mycoupon/available",
        views.AvailableUserCouponListView.as_view(),
        name="available-user-coupons",
    ),
    path(
        "mycoupon/<int:user_coupon_id>",
        views.UserCouponDetailView.as_view(),
        name="user-coupon-detail",
    ),
    path(
        "issue/<int:coupon_id>",
        views.UserCouponIssueView.as_view(),
        name="user-coupon-issue",
    ),
    path("", views.CouponListView.as_view(), name="coupon-list"),
    path("<int:coupon_id>", views.CouponDetailView.as_view(), name="coupon-detail"),
]
