from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser


class CouponListView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass


class CouponDetailView(APIView):
    def get(self, request, coupon_id):
        pass

    def put(self, request, coupon_id):
        pass

    def delete(self, request, coupon_id):
        pass


class UserCouponListView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass


class UserCouponDetailView(APIView):
    def get(self, request, user_coupon_id):
        pass

    def put(self, request, user_coupon_id):
        pass

    def delete(self, request, user_coupon_id):
        pass
