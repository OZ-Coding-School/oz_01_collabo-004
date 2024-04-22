from typing import Union

from django.db.models import Q
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.models import Category, CategoryProductConnector
from categories.serializers import CategorySerializer
from common.utils import S3ImgUploader

from .models import Product
from .serializers import ProductSerializer


class ProductListView(APIView):
    serializer_class = ProductSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request: Request) -> Response:
        product = Product.objects.filter(status=True).all()

        if not product.exists():
            return Response({"msg": "상품이 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get_object(self, product_id: int) -> Union[Product, Response]:
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "상품을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request: Request, product_id: int) -> Response:
        product = self.get_object(product_id)
        if product is not None:
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            return Response({"error": "상품을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request, product_id: int) -> Response:
        product = self.get_object(product_id)
        if product is not None:
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "상품을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, product_id: int) -> Response:
        product = self.get_object(product_id)
        if product is not None:
            # product.status = False  # type: ignore
            product.delete()  # type: ignore
            return Response(
                {"message": "상품이 성공적으로 삭제되었습니다."},
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response({"error": "상품을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)


class GetProductByCategoryView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request: Request, category_id: int) -> Response:
        try:
            queryset = Category.objects.filter(id=category_id).order_by("-id")
            paginator = PageNumberPagination()
            pagenated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = CategorySerializer(pagenated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductImageUploadView(APIView):
    def post(self, request: Request, product_id: int) -> Response:
        """
        이미지 업로드를 시도하면 boto3를 이용해서 s3로 이미지를 업로드하는 메서드
        """
        if "description_img" in request.FILES:
            image_file = request.FILES["description_img"]
            prefix = f"products/{product_id}/description_img/"
        elif "product_img" in request.FILES:
            image_file = request.FILES["product_img"]
            prefix = f"products/{product_id}/product_images/"
        try:
            image_uploader = S3ImgUploader()
            image_url = image_uploader.upload(image_file, prefix)
            return Response({"image_url": image_url}, status=status.HTTP_200_OK)
        except ValueError as ve:
            return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request: Request) -> Response:
        try:
            image_file_url = request.data.get("image_file_url")
            image_uploader = S3ImgUploader()
            response = image_uploader.delete_img_file(image_file_url)  # type: ignore

            if response["status"] in [200, 204]:
                return Response(response["msg"], status=status.HTTP_200_OK)
            return Response(response["msg"], status=response["status"])
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# 상품 검색 키워드나 카테고리에 충족하는 검색 기능
class ProductSearchView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request: Request) -> Response:
        keyword = request.query_params.get("keyword", "")
        category_id = request.query_params.get("ct", "")
        min_price = request.query_params.get("min_price", "")
        max_price = request.query_params.get("max_price", "")

        query = Product.objects.filter(price__gte=min_price, price__lte=max_price)

        if keyword:
            query = query.filter(Q(name__icontains=keyword) | Q(description_text__icontains=keyword))

        if category_id:
            query = query.filter(categoryproductconnector__category_id=category_id)

        serializer = ProductSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
