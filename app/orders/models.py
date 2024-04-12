import uuid

from django.db import models

from common.models import CommonModel
from coupons.models import UserCoupon
from products.models import Product
from users.models import User


# 주문
class Order(CommonModel):
    ORDER_CHOICES = (
        ("CANCEL", "cancel"),  # 주문 취소 상태
        ("PAID", "paid"),  # 결제 완료 상태
        ("ORDERED", "ordered"),  # 주문, 결제 미완 상태
    )
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sale_price = models.IntegerField(default=0)
    total_price = models.IntegerField()
    status = models.CharField(max_length=7, choices=ORDER_CHOICES, default="ordered")
    people = models.IntegerField(default=0)
    pet = models.IntegerField(default=0)
    pet_size_big = models.IntegerField(default=0)
    pet_size_medium = models.IntegerField(default=0)
    pet_size_small = models.IntegerField(default=0)
    departure_date = models.DateField(default=None)
    return_date = models.DateField(default=None)

    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_coupon = models.ForeignKey(UserCoupon, null=True, on_delete=models.SET_NULL)


class Payment(CommonModel):
    PAYMENT_STATUS_CHOICES = (
        ("PENDING", "pending"),  # 결제 대기중 상태
        ("SUCCESS", "success"),  # 결제 성공 상태
        ("FAILED", "failed"),  # 결제 실패 상태
        ("CANCELLED", "cancelled"),  # 결제 취소 신청 상태
        ("REFUNDED", "refunded"),  # 환불 완료 상태
    )

    PAYMENT_METHOD_CHOICES = (("credit_card", "신용카드"), ("bank_transfer", "무통장 입금"), ("toss_pay", "토스페이"))

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    amount = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
