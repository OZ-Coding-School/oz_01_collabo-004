import os
from datetime import datetime, timedelta

import requests
from django.contrib.auth import login
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from . import serializers
from .models import User


class Signup(APIView):
    serializer_class = serializers.UserSignUpSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        serializer = serializers.UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JWTLoginView(TokenObtainPairView):
    def post(self, request: Request) -> Response:
        response = super().post(request)
        refresh_token = response.data["refresh"]
        # 응답의 바디에 토큰값이 안들어가도록 객체에서 삭제.
        del response.data["refresh"]
        # jwt 토큰을 쿠키에 저장하도록함
        # access token 은 30분 단위로 만료되도록함
        # refresh token 은 하루 단위로 만료되도록함
        response.set_cookie(
            "AUT_REF",
            refresh_token,
            samesite=None,
            secure=False,
            httponly=False,
            expires=datetime.now() + timedelta(days=1),
        )
        response.status_code = status.HTTP_200_OK
        print(response.__dict__)
        return response


class JWTLogoutView(APIView):
    def post(self, request: Request) -> Response:
        try:
            # 응답으로 로그인한 사용자의 쿠키에서 토큰을 제거하는 설정
            response = Response(status=status.HTTP_200_OK)
            response.delete_cookie("AUT_REF")

            return response
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class JWTRefreshView(APIView):
    def post(self, request: Request) -> Response:
        refresh_token = request.COOKIES.get("AUT_REF")

        if not refresh_token:
            return Response({"msg": "required refresh token."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh_token_validate = RefreshToken(refresh_token)  # type: ignore
            access_token = str(refresh_token_validate.access_token)
            return Response({"access_token": access_token}, status=status.HTTP_200_OK)
        except:
            return Response(
                {"msg": "invalid refresh token. try login again"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserInfoSerializer

    def get(self, request: Request) -> Response:
        user = User.objects.get(id=request.user.id)  # type: ignore
        if user:
            serializer = serializers.UserInfoSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request) -> Response:
        serializer = serializers.UserInfoModifySerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request) -> Response:
        # 회원탈퇴 요청이 들어오면 상태를 False로 바꿔 탈퇴예정임을 나타내고
        # del_req_time 을 요청이 들어온 현재시간으로 세팅한다.
        # 이후 장고의 Cron을 이용하여 매일 정각에 삭제요청 후 시점이 6개월이 지난 데이터들을 삭제할 예정
        # 필드가 수정되고나면 로그아웃을 시킴
        try:
            user = request.user
            user.is_active = False
            user.del_req_time = datetime.now()  # type: ignore

            # 로그아웃
            response = Response(status=status.HTTP_200_OK)
            response.delete_cookie("AUT_REF")
            return response
        except Exception as e:
            return Response({"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class KakaoLoginView(APIView):
    def post(self, request: Request) -> Response:
        code = request.data.get("code")  # 프론트에서 보내준 코드
        # 카카오 oauth 토큰 발급 url로 code가 담긴 post 요청을 보내 응답을 받는다.
        token_response = requests.post(
            "https://kauth.kakao.com/oauth/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": "http://127.0.0.1:8000/kakao/callback",
                "client_id": os.environ.get("CLIENT_ID"),
            },
        )
        # 응답으로부터 액세스 토큰을 가져온다.
        access_token = token_response.json().get("access_token")

        user_data = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
            },
        )
        """
        1. 문제: 에러가 발생시 json데이터가 안올 수 있는데, 무조건 json()을 호출하면 시리얼라이저 에러가 발생할 가능성이 높다.
        2. 해결방법: 응답 받고 status_code를 확인한 후에 json() 호출, 500 or 400코드가 발생시 raise exception으로 탈출?
        """
        user_data_json = user_data.json()
        kakao_account = user_data_json["kakao_account"]
        profile = kakao_account.get("profile")
        try:
            user = User.objects.get(email=kakao_account.get("email"))
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            user = User.objects.create(
                email=kakao_account.get("email"),
                name=profile.get("nickname"),
                # avatar=profile.get("profile_image_url"),
            )
            user.set_unusable_password()
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
