from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from products.models import Product
from .models import ProductReview


class ProductReviewListTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            user_id="testuserid", password="password123", name="testname", email="test@example.com", phone="01012345678"
        )

        self.product_set = []

        for i in range(1, 21):
            product = Product.objects.create(
                name=f"testname{i}",
                description_text=f"testdescription{i}",
                price=int(f"{i}000000"),
            )
            self.product_set.append(product)

        self.review_set = []

        for i, product in enumerate(self.product_set):
            review = ProductReview.objects.create(
                user_id=self.user.id,
                product_id=product.id,
                title=f"testtitle{i+1}",
                content=f"testcontent{i+1}",
                status=True,
            )
            self.review_set.append(review)

        self.product = Product.objects.create(
            name="testname21",
            description_text="testdescription21",
            price=21000000,
        )

        self.token = AccessToken.for_user(self.user)
        self.client.force_login(user=self.user)

    def test_post_product_review(self):
        url = reverse("product-review-list")

        data = {"title": "serialize invalid case", "contents": "ummm...", "product": 'invalid type'}
        response = self.client.post(url, data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(ProductReview.objects.count(), 20)

        data = {"title": "testtitle21", "content": "testcontent21", "product_id": self.product.id}

        response = self.client.post(url, data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductReview.objects.count(), 21)
        self.assertEqual(response.data["title"], "testtitle21")
        self.assertEqual(response.data["content"], "testcontent21")
        self.assertEqual(response.data["product"], self.product.id)
        self.assertEqual(response.data['user'], self.user.id)

    def test_get_product_review(self):
        url = reverse("product-review-list")

        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)
        for i, review in enumerate(response.data['results']):
            self.assertEqual(review['user'], self.user.id)
            self.assertEqual(review['title'], self.review_set[i].title)
            self.assertEqual(review['content'], self.review_set[i].content)
            self.assertTrue(review["status"])
            self.assertEqual(review['product_info']['id'], self.product_set[i].id)
            self.assertEqual(review['product_info']['name'], self.product_set[i].name)
            self.assertEqual(review['product_info']['price'], self.product_set[i].price)
            self.assertEqual(review['product_info']['sale'], self.product_set[i].sale)
            self.assertEqual(review['product_info']['product_img'], self.product_set[i].product_img)


class ProductReviewDetailTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            user_id="testuserid",
            password="password123",
            name="testname",
            email="test@example.com",
            phone="01012345678"
        )

        self.product = Product.objects.create(
            name="testname",
            description_text="testdescription",
            price=1000000,
        )

        self.review = ProductReview.objects.create(
            user_id=self.user.id,
            product_id=self.product.id,
            title="testtitle",
            content="testcontent",
            status=True,
        )

        self.token = AccessToken.for_user(self.user)
        self.client.force_login(user=self.user)

    def test_get_product_review_detail(self):
        url = reverse("product-review-detail", kwargs={'product_id': self.product.id})
        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], self.user.id)
        self.assertEqual(response.data["title"], self.review.title)
        self.assertEqual(response.data["content"], self.review.content)
        self.assertTrue(response.data["status"])
        self.assertEqual(response.data["product"], self.review.product.id)

    def test_put_product_review_detail(self):
        url = reverse("product-review-detail", kwargs={'product_id': self.product.id})
        data = {
            'title': "testtitle_update",
            'content': "testcontent_update",
            'status': True
        }
        response = self.client.put(url, data=data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], self.user.id)
        self.assertEqual(response.data["product"], self.product.id)
        self.assertEqual(response.data["title"], "testtitle_update")
        self.assertEqual(response.data["content"], "testcontent_update")
        self.assertTrue(response.data["status"])
        self.assertEqual(ProductReview.objects.count(), 1)

        invalid_data = {
            'invalid_key': 'invalid_value',
            'name': 'invalid_value',
            'status': True
        }
        response = self.client.put(url, data=invalid_data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        url = reverse("product-review-detail", kwargs={'product_id': 9919283})
        response = self.client.delete(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(ProductReview.objects.count(), 1)

    def test_delete_product_review_detail(self):
        # 유효하지않은 상품 아이디인 경우
        url = reverse("product-review-detail", kwargs={'product_id': 810938091839})

        response = self.client.delete(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(ProductReview.objects.filter(status=True).count(), 1)

        # 유저가 구매한 상품인 경우
        url = reverse("product-review-detail", kwargs={'product_id': self.product.id})

        response = self.client.delete(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductReview.objects.filter(status=True).count(), 0)



