from django.db import models
from common.models import CommonModel
from users.models import User
from products.models import Product

class Wishlist(CommonModel):
    status = models.BooleanField(null=False, default=False)

    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
