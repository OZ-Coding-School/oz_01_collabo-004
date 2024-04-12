from typing import Union

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from .serializers import CategorySerializer


class CategoryListView(APIView):
    def get(self, request: Request) -> Response:
        category = Category.objects.all()
        if not category.exists():
            Response(
                {"msg": "There are no registered categories."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    def get_object(self, category_pk: int) -> Union[Category, Response]:
        try:
            return Category.objects.get(id=category_pk)
        except Category.DoesNotExist:
            return Response(
                {"msg": "There is no part count for this category."},
                status=status.HTTP_404_NOT_FOUND,
            )

    def get(self, request: Request, category_pk: int) -> Response:
        category = self.get_object(category_pk)
        if category is not None:
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"msg": "There is no part count for this category."},
            status=status.HTTP_404_NOT_FOUND,
        )

    def put(self, request: Request, category_pk: int) -> Response:
        category = self.get_object(category_pk)

        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, category_pk: int) -> Response:
        category = self.get_object(category_pk)
        category.delete()  # type: ignore
        return Response(status=status.HTTP_200_OK)
