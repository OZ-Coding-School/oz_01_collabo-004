from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from . import serializers
from datetime import datetime, timedelta
from .models import User

    
class Signup(APIView):
    def post(self, request):
        user_data = request.data
        serializer = serializers.UserSignUpSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JWTLoginView(TokenObtainPairView):
    def post(self, request):
        response = super().post(request)
        refresh_token = response.data['refresh']
        # 응답의 바디에 토큰값이 안들어가도록 객체에서 삭제.
        del response.data['refresh']
        # jwt 토큰을 쿠키에 저장하도록함
        # access token 은 30분 단위로 만료되도록함
        # refresh token 은 하루 단위로 만료되도록함
        response.set_cookie('AUT_REF', refresh_token, expires=datetime.now() + timedelta(days=1))
        response.status_code = status.HTTP_200_OK
        print(response.__dict__)
        return response
    
class JWTLogoutView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # 응답으로 로그인한 사용자의 쿠키에서 토큰을 제거하는 설정
            response = Response(status=status.HTTP_200_OK)
            response.delete_cookie("AUT_REF")
            
            return response
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_data = request.user
        user = User.objects.get(user_id=user_data.user_id)
        if user:
            serializer = serializers.UserInfoSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request):
        serializer = serializers.UserInfoModifySerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
    # 회원탈퇴 요청이 들어오면 상태를 False로 바꿔 탈퇴예정임을 나타내고
    # del_req_time 을 요청이 들어온 현재시간으로 세팅한다.
    # 이후 장고의 Cron을 이용하여 매일 정각에 삭제요청 후 시점이 6개월이 지난 데이터들을 삭제할 예정 
    # 필드가 수정되고나면 로그아웃을 시킴
        user = request.user
        data = {
            'is_active': False,
            'del_req_time': datetime.now()
        }
        serializer = serializers.UserDeleteSerializer(user, data)
        if serializer.is_valid():
            serializer.save()
            # 로그아웃
            response = Response(status=status.HTTP_200_OK)
            response.delete_cookie('AUT_REF')
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)