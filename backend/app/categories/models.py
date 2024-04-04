from common.models import CommonModel
from django.db import models
from products.models import Product
from users.models import User


class Category(CommonModel):
    name = models.CharField(max_length=100)
    product = models.ManyToManyField(Product)
    user = models.ManyToManyField(User)


class UserConnector(CommonModel):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
