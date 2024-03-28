from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
# 사용자
class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(unique=True, max_length=15)
    email = models.EmailField(unique=True, max_length=30)
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=20)
    ##category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    USERNAME_FIELD = 'user_id'
