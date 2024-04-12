from datetime import timedelta

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from coupons.models import Coupon, UserCoupon
from orders.models import Order
from products.models import Product


class OrderListTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            user_id="testuser", password="password123", name="testname", email="test@example.com", phone="0101010011"
        )
        self.product = Product.objects.create(name="testproduct", price=100000, status=True)
        self.product2 = Product.objects.create(name="testproduct2", price=200000, status=True)
        self.coupon = Coupon.objects.create(type="WELCOME", content="회원가입 축하 쿠폰", sale_price=10000, duration=30)
        self.user_coupon = UserCoupon.objects.create(
            user_id=self.user.pk, coupon_id=self.coupon.id, expired_at=self.coupon.get_expire_date()
        )
        self.token = AccessToken.for_user(self.user)

    def test_post_order_list(self) -> None:
        url = reverse("order-list")
        data = {
            "product": self.product.pk,
            "people": 2,
            "pet": 3,
            "pet_size_small": 1,
            "pet_size_medium": 1,
            "pet_size_big": 1,
            "departure_date": "2024-04-21",
            "return_date": "2024-04-23",
        }
        # 쿠폰을 사용하지 않은 정상적인 주문 요청
        response = self.client.post(url, data, headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["people"], 2)
        self.assertEqual(response.data["pet"], 3)
        self.assertEqual(response.data["pet_size_small"], 1)
        self.assertEqual(response.data["pet_size_medium"], 1)
        self.assertEqual(response.data["pet_size_big"], 1)
        self.assertEqual(response.data["departure_date"], "2024-04-21")
        self.assertEqual(response.data["return_date"], "2024-04-23")

        # 쿠폰을 사용한 정상적인 주문 요청
        data["user_coupon"] = self.user_coupon.pk
        response = self.client.post(url, data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user_coupon"], self.user_coupon.id)
        self.assertEqual(response.data["people"], 2)
        self.assertEqual(response.data["pet"], 3)
        self.assertEqual(response.data["pet_size_small"], 1)
        self.assertEqual(response.data["pet_size_medium"], 1)
        self.assertEqual(response.data["pet_size_big"], 1)
        self.assertEqual(response.data["departure_date"], "2024-04-21")
        self.assertEqual(response.data["return_date"], "2024-04-23")

        # 주문시 쿠폰을 적용하려 했지만 만료된 경우
        self.user_coupon.expired_at -= timedelta(days=31)
        self.user_coupon.save()
        response = self.client.post(url, data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "coupon has expired.")

        # 주문시 쿠폰을 사용하려 했지만 이미 사용된 쿠폰인 경우
        self.user_coupon.expired_at = self.coupon.get_expire_date()
        self.user_coupon.status = False
        self.user_coupon.save()
        response = self.client.post(url, data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "already used coupon.")

        # product_id가 유효하지않은경우
        data["product"] = 1233121414
        response = self.client.post(url, data, headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "plz check product_id")

        # 입력한 반려 동물 수와 선택한 반려동물 사이즈 수의 합이 다를 경우
        data["pet"] = 4
        response = self.client.post(url, data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "plz check pet size count & pet count.")

    def test_get_order_list(self) -> None:
        self.order1 = Order.objects.create(
            product_id=self.product.pk,
            user_id=self.user.pk,
            total_price=self.product.price,
            people=2,
            pet=3,
            pet_size_small=1,
            pet_size_medium=1,
            pet_size_big=1,
            departure_date="2024-04-21",
            return_date="2024-04-23",
        )
        self.order2 = Order.objects.create(
            product_id=self.product2.pk,
            user_id=self.user.pk,
            user_coupon_id=self.user_coupon.pk,
            total_price=self.product2.price,
            people=3,
            pet=4,
            pet_size_small=2,
            pet_size_medium=1,
            pet_size_big=1,
            departure_date="2024-04-30",
            return_date="2024-05-03",
        )

        url = reverse("order-list")
        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["total_price"], self.product.price)
        self.assertEqual(response.data[0]["people"], 2)
        self.assertEqual(response.data[0]["pet"], 3)
        self.assertEqual(response.data[0]["status"], "ordered")
        self.assertEqual(response.data[1]["total_price"], self.product2.price)
        self.assertEqual(response.data[1]["people"], 3)
        self.assertEqual(response.data[1]["pet"], 4)
        self.assertEqual(response.data[1]["status"], "ordered")
        self.assertEqual(response.data[0]["product_info"]["id"], response.data[0]["product"])
        self.assertEqual(Order.objects.count(), 2)


class OrderDetailViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            user_id="testuser", password="password123", name="testname", email="test@example.com", phone="0101010011"
        )
        self.user2 = get_user_model().objects.create_user(
            user_id="testuser2", password="password123", name="testname2", email="test2@example.com", phone="0101010012"
        )
        self.product = Product.objects.create(name="testproduct", price=100000, status=True)
        self.coupon = Coupon.objects.create(type="WELCOME", content="회원가입 축하 쿠폰", sale_price=10000, duration=30)
        self.user_coupon = UserCoupon.objects.create(
            user_id=self.user.pk, coupon_id=self.coupon.pk, expired_at=self.coupon.get_expire_date()
        )
        self.order = Order.objects.create(
            product_id=self.product.pk,
            user_id=self.user.pk,
            total_price=self.product.price,
            people=2,
            pet=3,
            pet_size_small=1,
            pet_size_medium=1,
            pet_size_big=1,
            departure_date="2024-04-21",
            return_date="2024-04-23",
            status="ORDERED",
        )
        self.order2 = Order.objects.create(
            product_id=self.product.pk,
            user_id=self.user.pk,
            total_price=self.product.price,
            people=2,
            pet=3,
            pet_size_small=1,
            pet_size_medium=1,
            pet_size_big=1,
            departure_date="2024-04-21",
            return_date="2024-04-23",
            status="CANCEL",
        )
        self.order3 = Order.objects.create(
            product_id=self.product.pk,
            user_id=self.user2.pk,
            total_price=self.product.price,
            people=2,
            pet=3,
            pet_size_small=1,
            pet_size_medium=1,
            pet_size_big=1,
            departure_date="2024-04-21",
            return_date="2024-04-23",
            status="PAID",
        )
        self.token = AccessToken.for_user(self.user)

    def test_order_detail_get(self) -> None:
        # 유저가 주문한 내역을 조회
        url = reverse("order-detail", kwargs={"order_id": self.order.order_id})
        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data["product"], self.product.pk)
        self.assertEqual(response.data["user"], self.user.pk)
        self.assertEqual(response.data["total_price"], self.product.price)
        self.assertEqual(response.data["people"], 2)
        self.assertEqual(response.data["pet"], 3)
        self.assertEqual(response.data["pet_size_small"], 1)
        self.assertEqual(response.data["pet_size_medium"], 1)
        self.assertEqual(response.data["pet_size_big"], 1)
        self.assertEqual(response.data["departure_date"], "2024-04-21")
        self.assertEqual(response.data["return_date"], "2024-04-23")

        # 존재하지 않는 order_id를 조회하려고 시도할 때
        url = reverse("order-detail", kwargs={"order_id": "5e30ea2a-1e85-40e1-a9c7-19e5a6db9c94"})
        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # order_id가 uuid형식이 아닐 때
        url = reverse("order-detail", kwargs={"order_id": "213j4123a"})
        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "Invalid order_id")

        # 다른 유저의 주문 정보를 조회하려고 시도할 때
        url = reverse("order-detail", kwargs={"order_id": self.order3.order_id})
        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_order_detail_put(self) -> None:
        data = {
            "people": 3,
            "pet": 2,
            "pet_size_small": 1,
            "pet_size_medium": 1,
            "pet_size_big": 0,
            "departure_date": "2024-04-23",
            "return_date": "2024-04-26",
        }
        # 유저가 주문한 주문내역의 옵션 수정
        url = reverse("order-detail", kwargs={"order_id": self.order.order_id})
        response = self.client.put(url, data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["people"], 3)
        self.assertEqual(response.data["pet"], 2)
        self.assertEqual(response.data["pet_size_small"], 1)
        self.assertEqual(response.data["pet_size_medium"], 1)
        self.assertEqual(response.data["pet_size_big"], 0)
        self.assertEqual(response.data["departure_date"], "2024-04-23")
        self.assertEqual(response.data["return_date"], "2024-04-26")

        # 이미 취소된 주문에 대해서 수정을 시도하려고 할 때
        url = reverse("order-detail", kwargs={"order_id": self.order2.order_id})
        response = self.client.put(url, data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "already canceled order.")

        # 이미 결제된 주문에 대해서 수정을 시도하려고 할 때
        self.order2.status = "PAID"
        self.order2.save()
        response = self.client.put(url, data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "already paid order.")

    def test_order_detail_delete(self) -> None:
        # 'ORDERED' 상태의 주문 취소시 주문의 상태를 'CANCEL' 로 바꾸는지 테스트
        url = reverse("order-detail", kwargs={"order_id": self.order.order_id})
        response = self.client.delete(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "Successfully Canceled")

        # 'PAID' 상태의 주문 취소시 주문의 상태를 'CANCEL' 로 바꾸는지 테스트
        self.order.status = "PAID"
        self.order.save()
        response = self.client.delete(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["msg"], "Successfully Canceled")

        # 'CANCEL' 상태의 주문 취소 요청시 적절한 응답을 반환하는지 테스트
        url = reverse("order-detail", kwargs={"order_id": self.order2.order_id})
        response = self.client.delete(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "already cancelled")
