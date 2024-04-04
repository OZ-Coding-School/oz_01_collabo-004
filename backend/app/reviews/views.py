from config.paginations import ProductReviewPagination
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import ProductReview
from .serializers import ProductReviewListSerializer, ProductReviewDetailSerializer


class ProductReviewListView(APIView):
    serializer_class = ProductReviewListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

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
            "content": request.data.get("content")
        }
        serializer = ProductReviewListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductReviewDetailView(APIView):
    serializer_class = ProductReviewDetailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, product_id, *args, **kwargs):
        try:
            review = ProductReview.objects.get(user_id=request.user.id, product_id=product_id)
            serializer = ProductReviewDetailSerializer(review)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, product_id, *args):
        try:
            review = ProductReview.objects.get(user_id=request.user.id, product_id=product_id)

        except ProductReview.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductReviewDetailSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id, *args):
        try:
            review = ProductReview.objects.get(user_id=request.user.id, product_id=product_id)
        except ProductReview.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        review.status = False
        review.save()
        return Response(status=status.HTTP_200_OK)
