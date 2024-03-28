from django.db import models
from common.models import CommonModel
from products.models import Product
from users.models import User

# 주문
class Orders(CommonModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    sale_price = models.IntegerField()
    total_price = models.IntegerField()
    status = models.BooleanField(default=False)
    