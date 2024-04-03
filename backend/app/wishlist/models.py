from django.db import models
from common.models import CommonModel
from users.models import User
from products.models import Product


class Wishlist(CommonModel):
    status = models.BooleanField(default=True)

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
