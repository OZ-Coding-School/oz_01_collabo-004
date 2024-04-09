from django.db import models
from django.utils import timezone

from common.models import CommonModel
from users.models import User


class Coupon(CommonModel):
    COUPONS_CHOICES = (
        ("EVENT", "event"),  # 이벤트 쿠폰
        ("WELCOME", "welcome"),  # 웰컴 쿠폰(회원가입시)
        ("REGULAR", "regular"),  # 정기 쿠폰(ex. 월마다, 계절별 등)
    )
    type = models.CharField(max_length=7, choices=COUPONS_CHOICES)  # 쿠폰의 종류를 나타낼 필드(웰컴, 이벤트, 정기 등)
    content = models.CharField(max_length=50)  # 어떤 쿠폰인지 기술할 필드
    sale_price = models.IntegerField()  # 쿠폰의 할인 금액
    duration = models.PositiveIntegerField()  # 쿠폰의 유효기간(일 수로)을 나타낼 수 있는 필드

    def get_expire_date(self):
        # 쿠폰 발행일로부터 유효기간(duration)을 더하여 만료일을 계산
        return self.created_at + timezone.timedelta(days=self.duration)


class UserCoupon(CommonModel):
    status = models.BooleanField(default=True)  # 쿠폰의 사용가능 상태 (True - 사용가능, False - 사용불가)
    expired_at = models.DateTimeField()  # 쿠폰의 만료일을 나타낼 수 있는 필드

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저의 정보를 가져올 필드
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)  # 쿠폰의 정보를 가져올 필드
