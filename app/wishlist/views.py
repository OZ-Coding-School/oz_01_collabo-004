from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from wishlist.serializers import CreateWishlistSerializer, WishlistSerializer

from .models import Wishlist


class WishlistView(APIView):
    # 위시리스트 목록 가져오기
    @extend_schema(responses=WishlistSerializer(many=True), description="Read all Wishlist for login_user")
    def get(self, request: Request) -> Response:
        wishlist = Wishlist.objects.filter(user_id=request.user.id, status=True).all()  # type: ignore
        if wishlist:
            serializer = WishlistSerializer(wishlist, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    # 위시리스트 저장하기
    @extend_schema(
        request=CreateWishlistSerializer, responses=CreateWishlistSerializer, description="Create a new wishlist"
    )
    def post(self, request: Request) -> Response:
        data = {
            "product": request.data.get("product"),
        }
        serializer = CreateWishlistSerializer(data=data)

        if serializer.is_valid():
            # 기존에 위시리스트에 추가되어있던 경우
            # 기존에 위시리스트에 추가된 상품이 있으면 해당 상품의 위시리스트 상태를 확인.
            # 위시리스트 상태가 True이면 이미 위시리스트에 존재한다고 알림.
            # False 이면 상태를 변경해주고 성공적으로 위시리스트에 추가되었다고 알림.
            check_wishlist = Wishlist.objects.filter(  # type: ignore
                user_id=request.user.id, product_id=serializer.validated_data["product"]
            ).first()
            if check_wishlist:
                check_wishlist.status = not check_wishlist.status
                check_wishlist.save()
                serializer = CreateWishlistSerializer(check_wishlist)
                return Response(serializer.data, status=status.HTTP_200_OK)
            # 기존에 위시리스트에 추가되지 않은 경우 새로운 위시리스트 생성
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WishlistDetailView(APIView):
    # 위시리스트의 상품 상세내역
    @extend_schema(responses=WishlistSerializer, description="위시리스트의 상세 조회(마이페이지용)")
    def get(self, request: Request, wishlist_id: int) -> Response:
        wishlist_product = get_object_or_404(Wishlist, id=wishlist_id, user_id=request.user.id, status=True)
        serializer = WishlistSerializer(wishlist_product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 위시리스트 삭제하기
    @extend_schema(description="위시리스트의 삭제(마이페이지용)")
    def put(self, request: Request, wishlist_id: int) -> Response:
        wishlist = get_object_or_404(Wishlist, id=wishlist_id, user_id=request.user.id)
        if not wishlist.status:
            return Response({"msg": "already deleted"}, status=status.HTTP_400_BAD_REQUEST)
        wishlist.status = False
        wishlist.save()
        return Response(status=status.HTTP_200_OK)
