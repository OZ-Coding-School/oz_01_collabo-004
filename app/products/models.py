from django.db import models

from common.models import CommonModel


class Product(CommonModel):
    name = models.CharField(max_length=100)
    product_img = models.URLField(null=True, default=None)
    description_img = models.URLField(null=True, default=None)
    description_text = models.TextField(null=True, default=None)
    price = models.IntegerField()
    sale = models.IntegerField(null=True, default=0)
    view_count = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
