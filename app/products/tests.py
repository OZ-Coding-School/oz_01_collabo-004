from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.test import APITestCase

from categories.models import Category, CategoryProductConnector

from .models import Product
from .serializers import ProductSerializer

# class ProductAPITestCase(APITestCase):
#     def setUp(self):
#         self.products_url = reverse('product-list-create')
#         self.product1 = Product.objects.create(name='상품1', description='상품1 설명', price=10000)
#         self.product2 = Product.objects.create(name='상품2', description='상품2 설명', price=20000)

#     def test_get_product_list(self):
#         response = self.client.get(self.products_url)
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)

#     def test_create_product(self):
#         data = {'name': '새로운 상품', 'description': '새로운 상품 설명', 'price': 30000}
#         response = self.client.post(self.products_url, data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Product.objects.count(), 3)

#     def test_get_product_detail(self):
#         product_url = reverse('product-detail', args=[self.product1.id])
#         response = self.client.get(product_url)
#         serializer = ProductSerializer(self.product1)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)

#     def test_update_product(self):
#         product_url = reverse('product-detail', args=[self.product1.id])
#         data = {'name': '수정된 상품', 'description': '수정된 상품 설명', 'price': 15000}
#         response = self.client.put(product_url, data, format='json')
#         updated_product = Product.objects.get(id=self.product1.id)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(updated_product.name, '수정된 상품')

#     def test_delete_product(self):
#         product_url = reverse('product-detail', args=[self.product1.id])
#         response = self.client.delete(product_url)

#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Product.objects.count(), 1)


class ProductSearchTest(APITestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name="TestCategory")

        self.product1 = Product.objects.create(name="상품1one", description_text="상품1 설명", price=30)
        self.product2 = Product.objects.create(name="상품2two", description_text="상품2 설명", price=80)
        self.product3 = Product.objects.create(name="상품3three", description_text="상품2 설명", price=80)

        CategoryProductConnector.objects.create(product=self.product1, category=self.category)
        CategoryProductConnector.objects.create(product=self.product2, category=self.category)
        CategoryProductConnector.objects.create(product=self.product3, category=self.category)

    def test_키워드_상품_검색(self) -> None:
        url = reverse("product-search")
        keyword = ["two"]
        query_test = {
            "keyword": keyword,
            "min_price": "30",
            "max_price": "100",
        }

        response = self.client.get(url, query_test)
        if not response.data:
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_카테고리_상품_검색(self) -> None:
        url = reverse("product-search")
        query_test = {
            "ct": "1",
            "min_price": "30",
            "max_price": "50",
        }

        response = self.client.get(url, query_test)
        if not response.data:
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
