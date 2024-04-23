from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from . import views

urlpatterns = [
    path("login/", views.JWTLoginView.as_view(), name="jwt_login"),
    path("logout/", views.JWTLogoutView.as_view(), name="jwt_logout"),
    path("simple/jwt_refresh_token", views.JWTRefreshView.as_view(), name="refresh_token"),
    path("simple/jwt_verify_token", TokenVerifyView.as_view(), name="token_verify"),
    path("signup/", views.Signup.as_view(), name="signup"),
    path("info/", views.UserDetailView.as_view(), name="user_detail"),
    path("email-verify/send/", views.SendVerificationCodeView.as_view(), name="send_verify_code"),
    path("email-verify/forgot-password/", views.ForgotPasswordView.as_view(), name="forgot_password"),
    path("email-verify/", views.VerifyCodeView.as_view(), name="email_verify"),
    path("auth/kakao_login/", views.KakaoLoginView.as_view(), name="kakao_login"),
]
