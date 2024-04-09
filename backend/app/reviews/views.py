from config.paginations import ProductReviewPagination
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .models import ProductReview
from .serializers import ProductReviewDetailSerializer, ProductReviewListSerializer


class ProductReviewListView(APIView):
    serializer_class = ProductReviewListSerializer

    def get(self, request, *args, **kwargs):
        try:
            queryset = ProductReview.objects.filter(user_id=request.user.id).all()
            paginator = ProductReviewPagination()
            pagenated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = ProductReviewListSerializer(pagenated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({"msg": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        data = {
            "user": request.user.id,
            "product": request.data.get("product_id"),
            "title": request.data.get("title"),
            "content": request.data.get("content"),
        }
        serializer = ProductReviewListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductReviewDetailView(APIView):
    serializer_class = ProductReviewDetailSerializer

    def get(self, request, review_id, *args, **kwargs):
        review = get_object_or_404(ProductReview, id=review_id)
        serializer = ProductReviewDetailSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, review_id, *args):
        review = get_object_or_404(ProductReview, id=review_id)
        if review.user == request.user:  # 리뷰를 작성한 유저가 보낸 수정 요청인지를 확인함
            serializer = ProductReviewDetailSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, review_id, *args):
        review = get_object_or_404(ProductReview, id=review_id)
        if review.user == request.user:  # 리뷰를 작성한 유저가 보낸 삭제요청인지를 확인함
            review.status = False
            review.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


