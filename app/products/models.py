from django.db import models

from common.models import CommonModel


class Product(CommonModel):
    name = models.CharField(max_length=100)
    product_img = models.ImageField(upload_to="product/img/thumbnail", default=None)
    description_img = models.ImageField(upload_to="product/img/description", default=None)
    description_text = models.TextField(default=None)
    price = models.IntegerField(default=0)
    travel_period = models.IntegerField(default=0)
    sale = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
