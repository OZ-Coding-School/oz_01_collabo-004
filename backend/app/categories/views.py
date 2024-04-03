from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer


class CategoryListView(APIView):
    def get(self, request):
        categroy = Category.objects.all()
        if not categroy.exists():
            Response({"error":"해당 카테고리를 찾을수 없읍니다."}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = CategorySerializer(categroy, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error":"해당 카테고리를 찾을수 없습니다"}, status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        else:
            return Response({"error":"해당 카테고리를 찾을수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)