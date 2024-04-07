import pdb

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Wishlist
from .serializers import CreateWishlistSerializer, WishlistSerializer


def get_wishlist(user_id, product_id):
    try:
        return Wishlist.objects.get(user_id=user_id, product_id=product_id)
    except Wishlist.DoesNotExist:
        return None


class WishlistView(APIView):
    # 위시리스트 목록 가져오기
    def get(self, request):
        wishlist = Wishlist.objects.filter(user_id=request.user.id, status=True).all()
        if wishlist:
            serializer = WishlistSerializer(wishlist, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    # 위시리스트 저장하기
    def post(self, request):
        data = {
            "user": request.user.id,
            "product": request.data.get("product_id"),
        }
        serializer = CreateWishlistSerializer(data=data)

        if serializer.is_valid():
            # 기존에 위시리스트에 추가되어있던 경우
            # 기존에 위시리스트에 추가된 상품이 있으면 해당 상품의 위시리스트 상태를 확인.
            # 위시리스트 상태가 True이면 이미 위시리스트에 존재한다고 알림.
            # False 이면 상태를 변경해주고 성공적으로 위시리스트에 추가되었다고 알림.
            check_wishlist = get_wishlist(user_id=request.user.id, product_id=request.data.get("product_id"))
            if check_wishlist:
                if check_wishlist.status == True:
                    return Response({"msg": "already added"}, status=status.HTTP_200_OK)
                check_wishlist.status = True
                check_wishlist.save()
                serializer = CreateWishlistSerializer(check_wishlist)
                return Response(serializer.data, status=status.HTTP_200_OK)
            # 기존에 위시리스트에 추가되지 않은 경우 새로운 위시리스트 생성
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WishlistDetailView(APIView):
    # 위시리스트의 상품 상세내역
    def get(self, request, product_id):
        wishlist_product = get_wishlist(user_id=request.user.id, product_id=product_id)
        if wishlist_product and wishlist_product.status == True:
            serializer = WishlistSerializer(wishlist_product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    # 위시리스트 삭제하기
    def delete(self, request, product_id):
        wishlist = get_wishlist(user_id=request.user.id, product_id=product_id)
        if wishlist:
            if not wishlist.status:
                return Response({"msg": "already deleted"}, status=status.HTTP_200_OK)
            wishlist.status = False
            wishlist.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
