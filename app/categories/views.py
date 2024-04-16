from typing import Union

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, CategoryUserConnector
from .serializers import (
    CategorySerializer,
    ProductConnectorSerializer,
    UserConnectorSerializer,
)


class CategoryListView(APIView):
    serializer_class = CategorySerializer

    def get(self, request):
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


class UserCategorySurveyView(APIView):

    def post(self, request):
        user = request.user
        if user.last_login is None:
            select_category_ids = request.data.getlist("select_category")
            if select_category_ids:
                connector_list = []
                for category_id in select_category_ids:
                    connector = CategoryUserConnector.objects.create(user_id=request.user.id, category_id=category_id)
                    connector_list.append(connector)
                serializer = UserConnectorSerializer(connector_list, many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"msg": "no category selected."}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# 유저가 자기가 선택한 카테고리 조회
class UserCategoryListView(APIView):
    def get(self, request, category_id):
        user = request.user
        connectors = CategoryUserConnector.objects.filter(category_id=category_id, user_id=request.user.id)
        if connectors:
            serializer = ProductConnectorSerializer(connectors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"msg": "no category selected."}, status=status.HTTP_404_NOT_FOUND)


# 유저가 자기가 선택한 카테고리 삭제
# 커넥터를 통해서 정보 가져오기
class UserCategoryDetailView(APIView):
    def delete(self, request, category_id):
        connector = CategoryUserConnector.objects.filter(category_id=category_id, user_id=request.user)
        if connector:
            connector.delete()
            return Response(status=status.HTTP_200_OK)
        return Response({"msg": "no category selected"}, status=status.HTTP_404_NOT_FOUND)
