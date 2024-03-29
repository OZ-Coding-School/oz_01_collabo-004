from common.models import CommonModel
from django.db import models


class Product(CommonModel):
    name = models.CharField(max_length=100)
    description_img = models.URLField(null=True, default=None)
    description_text = models.TextField(null=True, default=None)
    price = models.IntegerField()
    sale = models.IntegerField(null=True, default=None)
    view_count = models.IntegerField(null=False, default=0)
    status = models.BooleanField(null=False, default=False)

    