from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response

from coupons.models import UserCoupon


def coupon_apply(request, user_coupon_id):
    """
    유저가 쿠폰 사용시 status를 False로 바꿔주는 메서드
    """
    coupon = get_object_or_404(UserCoupon, id=user_coupon_id)
    if coupon.user_id != request.user.id:  # 요청을 보낸 유저가 쿠폰을 소지한 유저가 맞는지 확인
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    if coupon.status:
        if coupon.expired_at > timezone.now():
            coupon.status = False
            coupon.save()
            return Response({"msg": "successfully used coupon."}, status=status.HTTP_200_OK)
        return Response({"msg": "coupon has expired."}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"msg": "already used coupon."}, status=status.HTTP_400_BAD_REQUEST)
