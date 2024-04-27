from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from coupons.models import Coupon, UserCoupon
from coupons.serializers import CouponSerializer, UserCouponSerializer


class CouponListView(APIView):
    serializer_class = CouponSerializer
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        coupons = Coupon.objects.all()
        if coupons:
            serializer = CouponSerializer(coupons, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request: Request) -> Response:
        coupon_data = request.data
        serializer = CouponSerializer(data=coupon_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CouponDetailView(APIView):
    serializer_class = CouponSerializer
    permission_classes = [IsAdminUser]

    def get(self, request: Request, coupon_id: int) -> Response:
        coupon = get_object_or_404(Coupon, id=coupon_id)
        serializer = CouponSerializer(coupon)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, coupon_id: int) -> Response:
        coupon = get_object_or_404(Coupon, id=coupon_id)
        modify_data = request.data
        serializer = CouponSerializer(coupon, data=modify_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, coupon_id: int) -> Response:
        coupon = get_object_or_404(Coupon, id=coupon_id)
        coupon.delete()
        return Response(status=status.HTTP_200_OK)


class UserCouponListView(APIView):
    serializer_class = UserCouponSerializer

    def get(self, request: Request) -> Response:
        # 전체 쿠폰 중에서 사용가능한 순으로, 그 중에서도 유효 기간이 짧은 순으로 내려줌
        coupons = UserCoupon.objects.filter(user_id=request.user.id).order_by("-status", "expired_at")  # type: ignore
        if coupons:
            serializer = UserCouponSerializer(coupons, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class AvailableUserCouponListView(APIView):
    """
    유저가 보유 중인 쿠폰 중 사용가능한 리스트를 내려주는 View
    """

    serializer_class = UserCouponSerializer

    def get(self, request: Request) -> Response:
        # 사용가능한 쿠폰 중에서 유효기간이 짧은것부터 내려줌
        coupons = UserCoupon.objects.filter(user_id=request.user.id, status=True).order_by("expired_at")  # type: ignore
        if coupons:
            serializer = UserCouponSerializer(coupons, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class UsedUserCouponListView(APIView):
    """
    유저가 사용했던 쿠폰 리스트를 내려주는 View
    """

    serializer_class = UserCouponSerializer

    def get(self, request: Request) -> Response:
        # 가장 최근에 사용했던 쿠폰순으로 내려줌
        coupons = UserCoupon.objects.filter(user_id=request.user.id, status=False).order_by(  # type: ignore
            "-modified_at"
        )
        if coupons:
            serializer = UserCouponSerializer(coupons, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class UserCouponDetailView(APIView):
    """
    유저가 보유한 쿠폰의 상세정보를 내려줄 메서드
    """

    serializer_class = UserCouponSerializer

    def get(self, request: Request, user_coupon_id: int) -> Response:
        coupon = get_object_or_404(UserCoupon, id=user_coupon_id)
        if coupon.user_id != request.user.id:  # 요청을 보낸 유저가 쿠폰을 소지한 유저가 맞는지 확인
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserCouponSerializer(coupon)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def delete(self, request, user_coupon_id):
    """
    이미 사용한 유저의 쿠폰을 삭제해주는 메서드
    """
    #     coupon = get_object_or_404(UserCoupon, id=user_coupon_id)
    #     if coupon.user_id != request.user.id:  # 요청을 보낸 유저가 쿠폰을 소지한 유저가 맞는지 확인
    #         return Response(status=status.HTTP_401_UNAUTHORIZED)
    #     if not coupon.status:
    #         coupon.delete()
    #         return Response(status=status.HTTP_200_OK)
    #     return Response({"msg": "available coupon."}, status=status.HTTP_400_BAD_REQUEST)


class UserCouponIssueView(APIView):
    @extend_schema(
        description="""
        쿠폰 발급요청을 처리하는 View
        이미 생성되어있는 쿠폰이 있으면 400 응답과 메시지를 반환,
        없다면 쿠폰의 유효성을 검증하고, 시리얼라이저로 데이터의 유효성 검증 후에 생성.
        시리얼라이저에서 유효성 검증 실패시 400 상태 코드, 시리얼라이저의 error 메시지를 반환.
        생성이 완료되면 응답으로 생성된 쿠폰의 정보와, 201 상태코드 반환.
        """
    )
    def post(self, request: Request, coupon_id: int) -> Response:
        from django.db import IntegrityError

        try:
            user_coupon, created = UserCoupon.objects.get_or_create(
                coupon_id=coupon_id, user_id=request.user.id, status=True
            )
            if not created:
                return Response({"msg": "already issued coupon."}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"msg": "Successfully issued coupon."}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"msg": "Invalid Coupon_id"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"msg": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
