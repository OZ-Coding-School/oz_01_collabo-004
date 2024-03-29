from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, user_id, password, **extra_fields):
        if not user_id:
            raise ValueError('Users must have an email address')

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
    ##category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'

