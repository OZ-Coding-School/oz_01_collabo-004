from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, user_id, password, **extra_fields):
        if not user_id:
            raise ValueError("Users must have an email address")

        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, user_id, password):
        user = self.create_user(user_id, password)

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
    # 회원 탈퇴 요청시 6개월 이후에 회원정보가 db상에서 삭제되도록 할 예정
    is_active = models.BooleanField(default=True)  # 가입시 true, 탈퇴요청시 false
    del_req_time = models.DateTimeField(null=True)  # 회원탈퇴요청 시간
    ##category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "user_id"
