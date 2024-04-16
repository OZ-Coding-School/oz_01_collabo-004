"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(dotenv_path="./local.env")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

SITE_ID = 1  # 현재 Django 사이트의 고유 식별자를 설정

DJANGO_SYSTEM_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # 여러 도메인을 관리해주는 장고 내장 시스템
]

CUSTOM_USER_APPS = [
    "corsheaders",
    "users",
    "orders",
    "products",
    "reviews",
    "categories",
    "wishlist",
    "coupons",
    "allauth",  # 로그인, 로그아웃, 회원가입, 비밀번호 변경, 비밀번호 초기화 등과 같은 기본적인 사용자 인증 기능을 제공
    "allauth.account",  # 사용자의 계정 설정을 커스터마이징하고 관리
    "allauth.socialaccount",  # 소셜 로그인 및 회원가입 기능을 제공
    "allauth.socialaccount.providers.kakao",  # 카카오 로그인 제공
    "core",
    "storages",
    "rest_framework",
    "drf_spectacular",
    "rest_framework_simplejwt",
]

INSTALLED_APPS = CUSTOM_USER_APPS + DJANGO_SYSTEM_APPS

# 유저 관련 설정
AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION_EXPIRE_DAYS = 1

# 이메일 인증을 위한 설정
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("GOOGLE_EMAIL")
EMAIL_HOST_PASSWORD = os.environ.get("GOOGLE_EMAIL_PASS")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LOGIN_REDIRECT_URL = "/"  # 로그인 후에 메인페이지로 리다이렉트

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

from django.urls.base import reverse_lazy

# LOGIN_URL = reverse_lazy('users:login') # 로그인 페이지로 리다이렉트
# ACCOUNT_LOGOUT_REDIRECT_URL = reverse_lazy('users:login') # 로그아웃 후에 리다이렉트 될 경로

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# wsgi 설정
WSGI_APPLICATION = "config.wsgi.application"

# 데이터 베이스 설정
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": os.environ.get("DB_HOST"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
        "PORT": "3306",
    }
}

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 15,
}

# api 문서 설정
SPECTACULAR_SETTINGS = {
    "TITLE": "DogGo API Documentation",
    "DESCRIPTION": "This is a description of DogGo API",
}

# simple-jwt 설정
from datetime import timedelta

SIMPLE_JWT = {
    # 액세스 토큰의 유효 기간을 5분으로 설정합니다.
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    # 리프레시 토큰의 유효 기간을 1일로 설정합니다.
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    # 리프레시 토큰을 갱신할 때마다 새 토큰을 생성하지 않도록 설정합니다.
    "ROTATE_REFRESH_TOKENS": False,
    # 토큰을 갱신한 후 이전 토큰을 블랙리스트에 추가합니다.
    "BLACKLIST_AFTER_ROTATION": True,
    # JWT에 사용할 서명 알고리즘으로 HS256을 사용합니다.
    "ALGORITHM": "HS256",
    # JWT를 서명하는 데 사용할 키로 Django의 SECRET_KEY를 사용합니다.
    "SIGNING_KEY": SECRET_KEY,
    # JWT 검증에 사용할 키입니다. HS256 알고리즘에서는 None으로 설정됩니다.
    "VERIFYING_KEY": None,
    # 인증 헤더의 타입으로 'Bearer'를 사용합니다.
    # Authorization: Bearer <token>
    "AUTH_HEADER_TYPES": ("Bearer",),
    # 토큰에 포함될 사용자 식별자 필드로 'id'를 사용합니다.
    "USER_ID_FIELD": "user_id",
    # 토큰 클레임에서 사용자 식별자에 해당하는 키로 'user_id'를 사용합니다.
    "USER_ID_CLAIM": "user_id",
    # 사용할 토큰 클래스로 AccessToken을 사용합니다.
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# 스케줄러 : 정해놓은 시간에 해당 메서드가 실행되도록함
# CRONJOBS = [
#     ('0 0 * * *', 'your_app_name.cron.delete_old_users'),
# ]

# CORS 설정
# CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:3000/', 'http://127.0.0.1:8000/']
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

# AWS S3 설정

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")

DEFAULT_FILE_STORAGE = os.environ.get("DEFAULT_FILE_STORAGE")

STATIC_URL = "/static/static/"
MEDIA_URL = "/static/media/"

MEDIA_ROOT = "/vol/web/media"
STATIC_ROOT = "/vol/web/static"
