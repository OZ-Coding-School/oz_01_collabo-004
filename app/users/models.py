from typing import Any

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from common.utils import get_random_id


def upload_to_profile_image(instance, filename: str) -> str:  # type: ignore
    # 파일명은 랜덤한 8자리의 문자열과 업로드한 파일이름을 조합해서 만듦(유일성 보장)
    # 상품별로 리뷰 이미지를 분류
    return f"users/profile/images/{get_random_id()} + {filename}"


class UserManager(BaseUserManager["User"]):
    def create_user(self, user_id: str, password: str, **extra_fields: Any) -> "User":
        if not user_id:
            raise ValueError("Users must have an email address")

        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)

        return user

    def create_superuser(self, user_id: str, password: str, **extra_fields: Any) -> "User":
        user = self.create_user(user_id, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# 사용자
class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(unique=True, max_length=15)
    email = models.EmailField(unique=True, max_length=30)
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to=upload_to_profile_image, null=True, default=None)
    # 회원 탈퇴 요청시 6개월 이후에 회원정보가 db상에서 삭제되도록 할 예정
    is_active = models.BooleanField(default=True)  # 가입시 true, 탈퇴요청시 false
    del_req_time = models.DateTimeField(null=True)  # 회원탈퇴요청 시간

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "user_id"
