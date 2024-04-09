from django.db import models

from common.models import CommonModel
from products.models import Product
from users.models import User

# from coupons.models import Coupon
# from payments.models import Payment


# 주문
class Order(CommonModel):
    ORDER_CHOICES = (
        ("CANCEL", "cancel"),
        ("PAID", "paid"),
        ("ORDERED", "ordered"),
    )
    payment_method = models.CharField(max_length=100)
    sale_price = models.IntegerField()
    total_price = models.IntegerField()
    status = models.CharField(max_length=7, choices=ORDER_CHOICES)
    option_peoples = models.IntegerField(default=0)
    option_pets = models.IntegerField(default=0)
    pet_size_big = models.IntegerField(default=0)
    pet_size_medium = models.IntegerField(default=0)
    pet_size_small = models.IntegerField(default=0)

    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # coupon = models.ForeignKey('Coupon')
    # payment = models.ForeignKey('Payment')
