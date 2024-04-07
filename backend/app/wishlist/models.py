from common.models import CommonModel
from django.db import models
from products.models import Product
from users.models import User


class Wishlist(CommonModel):
    status = models.BooleanField(default=True)

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
