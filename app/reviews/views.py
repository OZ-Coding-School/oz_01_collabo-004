from typing import Any

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from common.utils import S3ImgUploader
from config.paginations import ProductReviewPagination

from .models import ProductReview
from .serializers import (
    CreateReviewSerializer,
    MyReviewListSerializer,
    ProductReviewDetailSerializer,
    ProductReviewListSerializer,
)


class MyReviewListView(APIView):
    @extend_schema(responses=MyReviewListSerializer, description="Read products reviews for login user")
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        try:
            queryset = ProductReview.objects.filter(user_id=request.user.id).order_by("id")  # type: ignore
            paginator = ProductReviewPagination()
            pagenated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = MyReviewListSerializer(pagenated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({"msg": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        request=CreateReviewSerializer,
        responses=CreateReviewSerializer,
        description="Get products reviews, After Post product-review",
    )
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = request.data
        image_file = request.FILES.get("image_file")
        if image_file:
            data["image_url"] = image_file
        serializer = CreateReviewSerializer(data=data, partial=True)
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
        review = get_object_or_404(ProductReview, id=review_id, user=request.user.id)
        update_data = request.data
        update_image = request.FILES.get("image_file")
        if update_image:
            update_data["image_url"] = update_image
        serializer = ProductReviewDetailSerializer(review, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if update_image:
            if review.image_url:
                image_uploader = S3ImgUploader()
                try:
                    image_uploader.delete_img_file(str(review.image_url))  # 기존의 리뷰 이미지를 삭제
                except Exception as e:
                    return Response({"msg": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer.save()  # 인스턴스가 저장되면서 s3에 새로운 이미지가 업로드됨.
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, review_id: int, *args: Any) -> Response:
        review = get_object_or_404(ProductReview, id=review_id)
        if review.user == request.user:  # 리뷰를 작성한 유저가 보낸 삭제요청인지를 확인함
            review.status = False
            review.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# class ProductReviewImageUploadView(APIView):
#     def post(self, request: Request) -> Response:
#         """
#         이미지 업로드를 시도하면 boto3를 이용해서 s3로 이미지를 업로드하는 메서드
#         """
#         try:
#             image_file = request.FILES["image"]
#             prefix = f"users/reviews/"
#             image_uploader = S3ImgUploader()
#             image_url = image_uploader.upload(image_file, prefix)
#             return Response({"image_url": image_url}, status=status.HTTP_200_OK)
#         except ValueError as ve:
#             return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#     def delete(self, request: Request) -> Response:
#         try:
#             image_file_url = request.data["image_file_url"]
#             image_uploader = S3ImgUploader()
#             response = image_uploader.delete_img_file(image_file_url)
#             if response["status"] in [200, 204]:
#                 return Response(response["msg"], status=status.HTTP_200_OK)
#             return Response(response["msg"], status=response["status"])
#         except Exception as e:
#             return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductReviewListView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @extend_schema(
        responses=ProductReviewListSerializer,
        description="상품의 상세 페이지에서 보여줄 리뷰 리스트를 내려주는 get 메서드",
    )
    def get(self, request: Request, product_id: int) -> Response:
        reviews = ProductReview.objects.filter(product_id=product_id)
        if reviews:
            serializer = ProductReviewListSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"msg": "Review not found"}, status=status.HTTP_404_NOT_FOUND)
