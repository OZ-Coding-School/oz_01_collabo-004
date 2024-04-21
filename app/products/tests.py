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
        self.category1 = Category.objects.create(name="TestCategory1")
        self.category2 = Category.objects.create(name="TestCategory2")

        self.product1 = Product.objects.create(name="상품1", description_text="상품1 설명", price=30)
        self.product2 = Product.objects.create(name="상품2", description_text="상품2 설명", price=50)
        self.product3 = Product.objects.create(name="상품3", description_text="상품3 설명", price=30)
        self.product4 = Product.objects.create(name="상품4", description_text="상품4 설명", price=50)

        CategoryProductConnector.objects.create(product=self.product1, category=self.category1)
        CategoryProductConnector.objects.create(product=self.product2, category=self.category1)
        CategoryProductConnector.objects.create(product=self.product3, category=self.category2)
        CategoryProductConnector.objects.create(product=self.product4, category=self.category2)

    def test_키워드_상품_검색(self) -> None:
        url = reverse("product-search")
        keyword = ["two"]
        query_test = {
            "keyword": keyword,
            "min_price": "30",
            "max_price": "100",
        }

        response = self.client.get(url, query_test)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_카테고리_상품_검색(self) -> None:
        url = reverse("product-search")
        query_test1: dict[str, str | int] = {
            "ct": self.category1.pk,
            "min_price": "30",
            "max_price": "50",
        }

        response = self.client.get(url, query_test1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_body = response.json()

        self.assertEqual(len(response_body), 2)
        self.assertEqual(response_body[0]["id"], self.product1.id)
        self.assertEqual(response_body[0]["name"], self.product1.name)
        self.assertEqual(response_body[0]["product_img"], self.product1.product_img)
        self.assertEqual(response_body[0]["description_text"], self.product1.description_text)
        self.assertEqual(response_body[0]["price"], self.product1.price)
        self.assertEqual(response_body[0]["travel_period"], self.product1.travel_period)
        self.assertEqual(response_body[0]["discount"], self.product1.discount)
        self.assertEqual(response_body[0]["view_count"], self.product1.view_count)
        self.assertEqual(response_body[0]["status"], self.product1.status)

        self.assertEqual(response_body[1]["id"], self.product2.id)
        self.assertEqual(response_body[1]["name"], self.product2.name)
        self.assertEqual(response_body[1]["product_img"], self.product2.product_img)
        self.assertEqual(response_body[1]["description_text"], self.product2.description_text)
        self.assertEqual(response_body[1]["price"], self.product2.price)
        self.assertEqual(response_body[1]["travel_period"], self.product2.travel_period)
        self.assertEqual(response_body[1]["discount"], self.product2.discount)
        self.assertEqual(response_body[1]["view_count"], self.product2.view_count)
        self.assertEqual(response_body[1]["status"], self.product2.status)

        query_test2: dict[str, str | int] = {
            "ct": self.category2.pk,
            "min_price": "30",
            "max_price": "50",
        }

        response = self.client.get(url, query_test2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_body = response.json()

        self.assertEqual(len(response_body), 2)
        self.assertEqual(response_body[0]["id"], self.product3.id)
        self.assertEqual(response_body[0]["name"], self.product3.name)
        self.assertEqual(response_body[0]["product_img"], self.product3.product_img)
        self.assertEqual(response_body[0]["description_text"], self.product3.description_text)
        self.assertEqual(response_body[0]["price"], self.product3.price)
        self.assertEqual(response_body[0]["travel_period"], self.product3.travel_period)
        self.assertEqual(response_body[0]["discount"], self.product3.discount)
        self.assertEqual(response_body[0]["view_count"], self.product3.view_count)
        self.assertEqual(response_body[0]["status"], self.product3.status)

        self.assertEqual(response_body[1]["id"], self.product4.id)
        self.assertEqual(response_body[1]["name"], self.product4.name)
        self.assertEqual(response_body[1]["product_img"], self.product4.product_img)
        self.assertEqual(response_body[1]["description_text"], self.product4.description_text)
        self.assertEqual(response_body[1]["price"], self.product4.price)
        self.assertEqual(response_body[1]["travel_period"], self.product4.travel_period)
        self.assertEqual(response_body[1]["discount"], self.product4.discount)
        self.assertEqual(response_body[1]["view_count"], self.product4.view_count)
        self.assertEqual(response_body[1]["status"], self.product4.status)
