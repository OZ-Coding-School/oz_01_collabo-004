from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from categories.models import Category, CategoryProductConnector

from .models import Product
from .views import ProductDetailView


class ProductListViewTest(APITestCase):
    def setUp(self) -> None:
        self.product1 = Product.objects.create(name="상품1", description_text="상품1 설명", price=100, status=True)
        self.product2 = Product.objects.create(name="상품2", description_text="상품2 설명", price=100, status=True)

    def test_상품_리스트_가져오기(self) -> None:
        url = reverse("product-list-create")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], self.product1.name)
        self.assertEqual(response.data[0]["description_text"], self.product1.description_text)
        self.assertEqual(response.data[0]["price"], self.product1.price)

    def test_상품_리스트_생성(self) -> None:
        url = reverse("product-list-create")
        data = {"name": "상품3", "description_text": "상품3 설명", "price": 100, "status": True}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 3)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["description_text"], data["description_text"])
        self.assertEqual(response.data["price"], data["price"])


class ProductDetailViewTest(APITestCase):
    def setUp(self) -> None:
        self.product1 = Product.objects.create(name="상품1", description_text="상품1 설명", price=100, status=True)

    def test_detail_objcet_상품_가져오기(self) -> None:
        product_id = self.product1.id
        product_object = ProductDetailView().get_object(product_id)

        self.assertIsInstance(product_object, Product)

    def test_detail_상품_가져오기(self) -> None:
        url = reverse("product-detail", kwargs={"product_id": self.product1.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.product1.name)
        self.assertEqual(response.data["description_text"], self.product1.description_text)
        self.assertEqual(response.data["price"], self.product1.price)

    def test_detail_상품_변경(self) -> None:
        data = {"name": "new 상품1", "description_text": "new 상품1 설명", "price": 50}
        url = reverse("product-detail", kwargs={"product_id": self.product1.id})

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["description_text"], data["description_text"])
        self.assertEqual(response.data["price"], data["price"])

    def test_detail_상품_삭제(self) -> None:
        url = reverse("product-detail", kwargs={"product_id": self.product1.id})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
        self.assertEqual(Product.objects.filter(status=True).count(), 0)


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
        self.assertEqual(response_body[0]["sale"], self.product1.sale)
        self.assertEqual(response_body[0]["view_count"], self.product1.view_count)
        self.assertEqual(response_body[0]["status"], self.product1.status)

        self.assertEqual(response_body[1]["id"], self.product2.id)
        self.assertEqual(response_body[1]["name"], self.product2.name)
        self.assertEqual(response_body[1]["product_img"], self.product2.product_img)
        self.assertEqual(response_body[1]["description_text"], self.product2.description_text)
        self.assertEqual(response_body[1]["price"], self.product2.price)
        self.assertEqual(response_body[1]["travel_period"], self.product2.travel_period)
        self.assertEqual(response_body[1]["sale"], self.product2.sale)
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
        self.assertEqual(response_body[0]["sale"], self.product3.sale)
        self.assertEqual(response_body[0]["view_count"], self.product3.view_count)
        self.assertEqual(response_body[0]["status"], self.product3.status)

        self.assertEqual(response_body[1]["id"], self.product4.id)
        self.assertEqual(response_body[1]["name"], self.product4.name)
        self.assertEqual(response_body[1]["product_img"], self.product4.product_img)
        self.assertEqual(response_body[1]["description_text"], self.product4.description_text)
        self.assertEqual(response_body[1]["price"], self.product4.price)
        self.assertEqual(response_body[1]["travel_period"], self.product4.travel_period)
        self.assertEqual(response_body[1]["sale"], self.product4.sale)
        self.assertEqual(response_body[1]["view_count"], self.product4.view_count)
        self.assertEqual(response_body[1]["status"], self.product4.status)
