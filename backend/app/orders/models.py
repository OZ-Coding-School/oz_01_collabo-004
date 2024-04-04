from common.models import CommonModel
from django.db import models
from products.models import Product
from users.models import User


# 주문
class Order(CommonModel):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    payment_method = models.CharField(max_length=100)
    sale_price = models.IntegerField()
    total_price = models.IntegerField()
    status = models.BooleanField(default=False)
