from common.models import CommonModel
from django.db import models
from products.models import Product
from users.models import User


class Category(CommonModel):
    name = models.CharField(max_length=20)


class CategoryUserConnector(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class CategoryProductConnector(CommonModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
