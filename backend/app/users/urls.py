from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('login/', views.JWTLoginView.as_view(), name='jwt_login'),
    path('logout/', views.JWTLogoutView.as_view(), name='jwt_logout'),
    path('simple/jwt_refresh_token', TokenRefreshView.as_view(), name='refresh_token'),
    path('simple/jwt_verify_token', TokenVerifyView.as_view(), name='token_verify'),
]
