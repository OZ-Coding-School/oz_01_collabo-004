from django.db import models

from common.models import CommonModel
from products.models import Product
from users.models import User


class ProductReview(CommonModel):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    image_url = models.URLField(blank=True, null=True)
    status = models.BooleanField(default=True)

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
