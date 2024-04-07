from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductSerializer


class ProductListView(APIView):
    serializer_class = ProductSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        product = Product.objects.all()

        if not product.exists():
            return Response(
                {"msg": "상품이 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        else:
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "상품을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )

    def get(self, request, product_id):
        product = self.get_object(product_id)
        if product is not None:
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            return Response(
                {"error": "상품을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, product_id):
        product = self.get_object(product_id)
        if product is not None:
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"error": "상품을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, product_id):
        product = self.get_object(product_id)
        if product is not None:
            product.status = False
            return Response(
                {"message": "상품이 성공적으로 삭제되었습니다."},
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                {"error": "상품을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )


class GetProductByCategoryView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, category_id):
        try:
            queryset = Product.objects.filter(category_id=category_id).all()
            paginator = PageNumberPagination()
            pagenated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = ProductSerializer(pagenated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ProductSearchView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        keyword = request.query_params.get("keyword", "")
        category_id = request.query_params.get("ct", "")
        min_price = request.query_params.get("min_price", "")
        max_price = request.query_params.get("max_price", "")
