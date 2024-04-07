from rest_framework.urls import path

urlpatterns = [
    path('', views.CouponListView.as_view(), name='coupon-list'),
    path('<int:coupon_id>/', views.CouponDetailView.as_view(), name='coupon-list'),
    path('user/', views.UserCouponListView.as_view(), name='user-coupon-list'),
    path('user/<int:usercoupon_id>', views.UserCouponDetailView.as_view(), name='user-coupon-detail')
]