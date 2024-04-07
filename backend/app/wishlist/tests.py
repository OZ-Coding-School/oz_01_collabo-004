from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from products.models import Product

from .models import Wishlist


class WishlistTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            user_id="testuserid",
            password="password123",
            name="testname",
            email="test@example.com",
            phone="01012345678",
        )
        self.product1 = Product.objects.create(
            name="testproduct1",
            price=100000,
            status=True,
        )

        self.product2 = Product.objects.create(
            name="testproduct2",
            price=200000,
            status=True,
        )

        self.product3 = Product.objects.create(
            name="testproduct3",
            price=300000,
            status=True,
        )

        self.token = AccessToken.for_user(self.user)
        self.client.force_login(user=self.user)

    def test_post_wishlist(self):
        # 위시리스트에 처음 넣는 경우 테스트
        url = reverse("wishlist")
        data = {"product_id": self.product1.id}
        response = self.client.post(
            url, data, headers={"Authorization": f"Bearer {self.token}"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data["status"])
        self.assertEqual(response.data["product"], self.product1.id)
        self.assertEqual(response.data["user"], self.user.id)

        # 이미 위시리스트에 있는 경우 테스트
        response = self.client.post(
            url, data, headers={"Authorization": f"Bearer {self.token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("already added", response.data["msg"])

        # 이미 위시리스트에 넣었다가 취소하고 다시 위시리스트에 추가하는 경우 테스트
        wishlist = Wishlist.objects.get(
            user_id=self.user.id, product_id=self.product1.id
        )
        wishlist.status = False
        wishlist.save()
        response = self.client.post(
            url, data, headers={"Authorization": f"Bearer {self.token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["status"])
        self.assertEqual(response.data["product"], self.product1.id)
        self.assertEqual(response.data["user"], self.user.id)

    def test_get_wishlist(self):
        Wishlist.objects.create(user_id=self.user.id, product_id=self.product1.id)
        Wishlist.objects.create(user_id=self.user.id, product_id=self.product2.id)
        Wishlist.objects.create(user_id=self.user.id, product_id=self.product3.id)

        url = reverse("wishlist")

        response = self.client.get(
            url, headers={"Authorization": f"Bearer {self.token}"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["product"]["id"], self.product1.id)
        self.assertEqual(response.data[1]["product"]["id"], self.product2.id)
        self.assertEqual(response.data[2]["product"]["id"], self.product3.id)
        self.assertEqual(response.data[0]["user"], self.user.id)
        self.assertTrue(all(item["status"] for item in response.data))


class WishlistDetailTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            user_id="testuserid",
            password="password123",
            name="testname",
            email="test@example.com",
            phone="01012345678",
        )

        self.product = Product.objects.create(
            name="testproduct1",
            price=100000,
            status=True,
        )

        self.wishlist = Wishlist.objects.create(
            user_id=self.user.id,
            product_id=self.product.id,
        )

        self.token = AccessToken.for_user(self.user)
        self.client.force_login(user=self.user)

    def test_get_wishlist_detail(self):
        url = reverse("wishlist_detail", kwargs={"product_id": self.product.id})
        response = self.client.get(
            url, headers={"Authorization": f"Bearer {self.token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["product"]["id"], self.product.id)
        self.assertEqual(response.data["product"]["name"], self.product.name)
        self.assertEqual(response.data["product"]["price"], self.product.price)
        self.assertEqual(response.data["product"]["status"], self.product.status)
        self.assertEqual(response.data["user"], self.user.id)

        url = reverse("wishlist_detail", kwargs={"product_id": 919919191911})
        response = self.client.get(
            url, headers={"Authorization": f"Bearer {self.token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_product_detail(self):
        url = reverse("wishlist_detail", kwargs={"product_id": self.product.id})
        response = self.client.delete(
            url, headers={"Authorization": f"Bearer {self.token}"}
        )
        deleted_wishlist = Wishlist.objects.get(
            user_id=self.user.id, product_id=self.product.id
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(deleted_wishlist.status)

        response = self.client.delete(
            url, headers={"Authorization": f"Bearer {self.token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "already deleted")

        url = reverse("wishlist_detail", kwargs={"product_id": 919919191911})
        response = self.client.get(
            url, headers={"Authorization": f"Bearer {self.token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
