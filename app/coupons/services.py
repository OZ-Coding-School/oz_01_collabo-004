from django.core.exceptions import ValidationError
from django.utils import timezone

from coupons.models import UserCoupon


def change_coupon_status(user_coupon_id: int, new_status: bool) -> int:
    """
    쿠폰의 상태를 변경하는 메서드
    만약 쿠폰이 유효하고 사용하려면 new_status = False로 받아 쿠폰을 사용 불가하도록 상태를 변경.
    만약 쿠폰이 유효하고 쿠폰변경, 사용취소 등의 이유로 쿠폰을 다시 돌려받으려고 한다면,
    new_status = True를 받아 쿠폰을 다시 사용하도록 변경.
    이후 coupon의 sale_price 정보를 사용가능하도록 리턴해준다.
    """
    try:
        user_coupon = UserCoupon.objects.get(id=user_coupon_id)
        if user_coupon.status == new_status:
            if new_status:
                raise ValidationError("Coupon is already available.")
            else:
                raise ValidationError("Coupon is already used.")
        if user_coupon.expired_at < timezone.now():  # type: ignore
            raise ValidationError("Coupon has expired.")

        user_coupon.status = new_status
        user_coupon.save()
        return user_coupon.coupon.sale_price
    except UserCoupon.DoesNotExist:
        raise ValidationError("Coupon does not exist.")
