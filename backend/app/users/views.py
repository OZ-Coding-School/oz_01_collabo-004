from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .serializers import UserSerializer
from .models import User

class Signup(APIView):
    def post(self, request):
        User.objects.create_user(email=request.data['email'], password=request.data['password'], nickname=request.data['nickname'])

        return Response(request.data, status=status.HTTP_201_CREATED)

class JWTLoginView(TokenObtainPairView):
    def post(self, request):
        response = super().post(request)
        refresh_token = response.data['refresh']
        access_token = response.data['access']
        return Response(
            {'refresh': refresh_token, 'access': access_token},
            status=status.HTTP_200_OK
        )

class JWTLogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            access_token = RefreshToken(refresh_token)
            access_token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, )