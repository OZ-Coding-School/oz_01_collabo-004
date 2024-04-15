from typing import Any

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from common.utils import S3ImgUploader
from config.paginations import ProductReviewPagination

from .models import ProductReview
from .serializers import (
    CreateReviewSerializer,
    ProductReviewDetailSerializer,
    ProductReviewListSerializer,
)


class ProductReviewListView(APIView):
    @extend_schema(responses=ProductReviewListSerializer, description="Read products reviews for login user")
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        try:
            queryset = ProductReview.objects.filter(user_id=request.user.id).order_by("id")  # type: ignore
            paginator = ProductReviewPagination()
            pagenated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = ProductReviewListSerializer(pagenated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({"msg": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=CreateReviewSerializer,
        responses=CreateReviewSerializer,
        description="Get products reviews, After Post product-review",
    )
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = {
            "product": request.data.get("product"),
            "title": request.data.get("title"),
            "content": request.data.get("content"),
        }
        serializer = CreateReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductReviewDetailView(APIView):
    serializer_class = ProductReviewDetailSerializer

    def get(self, request: Request, review_id: int, *args: Any, **kwargs: Any) -> Response:
        review = get_object_or_404(ProductReview, id=review_id)
        serializer = ProductReviewDetailSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, review_id: int, *args: Any) -> Response:
        review = get_object_or_404(ProductReview, id=review_id)
        if review.user == request.user:  # 리뷰를 작성한 유저가 보낸 수정 요청인지를 확인함
            serializer = ProductReviewDetailSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request: Request, review_id: int, *args: Any) -> Response:
        review = get_object_or_404(ProductReview, id=review_id)
        if review.user == request.user:  # 리뷰를 작성한 유저가 보낸 삭제요청인지를 확인함
            review.status = False
            review.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ProductReviewImageUploadView(APIView):
    def post(self, request: Request) -> Response:
        """
        이미지 업로드를 시도하면 boto3를 이용해서 s3로 이미지를 업로드하는 메서드
        """
        try:
            image_file = request.FILES["image"]
            prefix = f"users/reviews/"
            image_uploader = S3ImgUploader()
            image_url = image_uploader.upload(image_file, prefix)
            return Response({"image_url": image_url}, status=status.HTTP_200_OK)
        except ValueError as ve:
            return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request: Request) -> Response:
        try:
            image_file_url = request.data["image_file_url"]
            image_uploader = S3ImgUploader()
            response = image_uploader.delete_img_file(image_file_url)
            if response["status"] in [200, 204]:
                return Response(response["msg"], status=status.HTTP_200_OK)
            return Response(response["msg"], status=response["status"])
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
