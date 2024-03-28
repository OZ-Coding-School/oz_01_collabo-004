from django.db import models
from common.models import CommonModel
from products.models import Product
from users.models import User


class ProductReview(CommonModel):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    image_url = models.URLField(blank=True, null=True)

    product = models.ForeignKey(Product)
