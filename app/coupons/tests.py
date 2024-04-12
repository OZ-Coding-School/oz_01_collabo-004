from datetime import timedelta

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from .models import Coupon, UserCoupon


class CouponListViewTestCase(APITestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            user_id="testuserid",
            password="password123",
        )

        self.token = AccessToken.for_user(self.admin_user)

    def test_get_coupon_list(self):
        url = reverse("coupon-list")
        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        self.coupon = Coupon.objects.create(type="WELCOME", content="회원가입 축하 쿠폰", sale_price=10000, duration=30)
        self.coupon2 = Coupon.objects.create(type="EVENT", content="빅세일 이벤트 쿠폰", sale_price=30000, duration=7)

        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["type"], "WELCOME")
        self.assertEqual(response.data[0]["content"], "회원가입 축하 쿠폰")
        self.assertEqual(response.data[0]["sale_price"], 10000)
        self.assertEqual(response.data[0]["duration"], 30)

        self.assertEqual(response.data[1]["type"], "EVENT")
        self.assertEqual(response.data[1]["content"], "빅세일 이벤트 쿠폰")
        self.assertEqual(response.data[1]["sale_price"], 30000)
        self.assertEqual(response.data[1]["duration"], 7)

    def test_post_coupon_list(self):
        url = reverse("coupon-list")
        data = {
            "type": "REGULAR",
            "content": "정기 할인 쿠폰",
            "sale_price": 20000,
            "duration": 30,
        }
        response = self.client.post(url, data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["type"], "REGULAR")
        self.assertEqual(response.data["content"], "정기 할인 쿠폰")
        self.assertEqual(response.data["sale_price"], 20000)
        self.assertEqual(response.data["duration"], 30)
        self.assertEqual(Coupon.objects.all().count(), 1)


class CouponDetailViewTest(APITestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            user_id="testuserid",
            password="password123",
        )
        self.coupon = Coupon.objects.create(type="WELCOME", content="회원가입 축하 쿠폰", sale_price=10000, duration=30)
        self.coupon2 = Coupon.objects.create(type="EVENT", content="빅세일 이벤트 쿠폰", sale_price=30000, duration=7)

        self.token = AccessToken.for_user(self.admin_user)

    def test_get_coupon_detail(self):
        url = reverse("coupon-detail", kwargs={"coupon_id": self.coupon.pk})
        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["type"], "WELCOME")
        self.assertEqual(response.data["content"], "회원가입 축하 쿠폰")
        self.assertEqual(response.data["sale_price"], 10000)
        self.assertEqual(response.data["duration"], 30)

        url = reverse("coupon-detail", kwargs={"coupon_id": self.coupon2.pk})
        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["type"], "EVENT")
        self.assertEqual(response.data["content"], "빅세일 이벤트 쿠폰")
        self.assertEqual(response.data["sale_price"], 30000)
        self.assertEqual(response.data["duration"], 7)

        url = reverse("coupon-detail", kwargs={"coupon_id": 10201})
        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_coupon_detail(self):
        url = reverse("coupon-detail", kwargs={"coupon_id": self.coupon.pk})
        data = {"duration": 60, "sale_price": 30000}

        response = self.client.put(url, data=data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["type"], "WELCOME")
        self.assertEqual(response.data["content"], "회원가입 축하 쿠폰")
        self.assertEqual(response.data["sale_price"], 30000)
        self.assertEqual(response.data["duration"], 60)

        self.coupon.refresh_from_db()
        self.assertEqual(self.coupon.sale_price, 30000)
        self.assertEqual(self.coupon.duration, 60)

    def test_delete_coupon_detail(self):
        url = reverse("coupon-detail", kwargs={"coupon_id": self.coupon.pk})
        response = self.client.delete(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Coupon.objects.all().count(), 1)

        url = reverse("coupon-detail", kwargs={"coupon_id": self.coupon2.pk})
        response = self.client.delete(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Coupon.objects.all().count(), 0)

        url = reverse("coupon-detail", kwargs={"coupon_id": 10201})
        response = self.client.delete(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UserCouponTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            user_id="testuser",
            password="password123",
            name="testuser",
            email="test@example.com",
            phone="01012341234",
        )
        self.coupon = Coupon.objects.create(type="WELCOME", content="회원가입 축하 쿠폰", sale_price=10000, duration=30)
        self.coupon2 = Coupon.objects.create(type="EVENT", content="빅세일 이벤트 쿠폰", sale_price=30000, duration=7)
        self.token = AccessToken.for_user(self.user)

    def test_user_coupon_issue(self):
        # 처음 발급요청을 테스트
        url = reverse("user-coupon-issue", kwargs={"coupon_id": self.coupon.pk})
        response = self.client.post(url, headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["coupon_info"]["type"], "WELCOME")
        self.assertEqual(response.data["coupon_info"]["content"], "회원가입 축하 쿠폰")
        self.assertEqual(response.data["coupon_info"]["sale_price"], 10000)
        self.assertEqual(response.data["coupon_info"]["duration"], 30)
        self.assertEqual(response.data["user"], self.user.pk)
        self.assertEqual(response.data["coupon"], self.coupon.pk)
        self.assertEqual(UserCoupon.objects.filter(user_id=self.user.pk).count(), 1)
        # 이미 발급된 쿠폰이 있는데 발급요청을 하는 경우 테스트
        response = self.client.post(url, headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["msg"], "already issued coupon.")

    def test_user_coupon_list(self):
        url = reverse("user-coupon-list")
        UserCoupon.objects.create(user_id=self.user.pk, coupon_id=self.coupon.pk, expired_at=timezone.now())
        UserCoupon.objects.create(user_id=self.user.pk, coupon_id=self.coupon2.pk, expired_at=timezone.now())

        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["coupon_info"]["type"], "WELCOME")
        self.assertEqual(response.data[0]["coupon_info"]["content"], "회원가입 축하 쿠폰")
        self.assertEqual(response.data[0]["coupon_info"]["sale_price"], 10000)
        self.assertEqual(response.data[0]["coupon_info"]["duration"], 30)
        self.assertEqual(response.data[0]["user"], self.user.pk)
        self.assertEqual(response.data[0]["coupon"], self.coupon.pk)
        self.assertEqual(response.data[1]["coupon_info"]["type"], "EVENT")
        self.assertEqual(response.data[1]["coupon_info"]["content"], "빅세일 이벤트 쿠폰")
        self.assertEqual(response.data[1]["coupon_info"]["sale_price"], 30000)
        self.assertEqual(response.data[1]["coupon_info"]["duration"], 7)
        self.assertEqual(response.data[1]["user"], self.user.pk)
        self.assertEqual(response.data[1]["coupon"], self.coupon2.pk)

    def test_available_user_coupon_list(self):
        url = reverse("available-user-coupons")
        UserCoupon.objects.create(user_id=self.user.pk, coupon_id=self.coupon.pk, expired_at=timezone.now())
        UserCoupon.objects.create(user_id=self.user.pk, coupon_id=self.coupon2.pk, expired_at=timezone.now())

        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["coupon_info"]["type"], "WELCOME")
        self.assertEqual(response.data[0]["coupon_info"]["content"], "회원가입 축하 쿠폰")
        self.assertEqual(response.data[0]["coupon_info"]["sale_price"], 10000)
        self.assertEqual(response.data[0]["coupon_info"]["duration"], 30)
        self.assertEqual(response.data[0]["user"], self.user.pk)
        self.assertEqual(response.data[0]["coupon"], self.coupon.pk)
        self.assertEqual(response.data[1]["coupon_info"]["type"], "EVENT")
        self.assertEqual(response.data[1]["coupon_info"]["content"], "빅세일 이벤트 쿠폰")
        self.assertEqual(response.data[1]["coupon_info"]["sale_price"], 30000)
        self.assertEqual(response.data[1]["coupon_info"]["duration"], 7)
        self.assertEqual(response.data[1]["user"], self.user.pk)
        self.assertEqual(response.data[1]["coupon"], self.coupon2.pk)
        self.assertTrue(response.data[0]["expired_at"] < response.data[1]["expired_at"])

    def test_used_user_coupon_list(self):
        url = reverse("used-user-coupons")
        # 아무런 쿠폰을 소유하지 않았을때 테스트
        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # 사용가능한 쿠폰을 소유하고 있을 때 테스트
        UserCoupon.objects.create(user_id=self.user.pk, coupon_id=self.coupon.pk, expired_at=timezone.now())
        UserCoupon.objects.create(
            user_id=self.user.pk,
            coupon_id=self.coupon2.pk,
            expired_at=timezone.now(),
            status=False,
        )

        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["coupon_info"]["type"], "EVENT")
        self.assertEqual(response.data[0]["coupon_info"]["content"], "빅세일 이벤트 쿠폰")
        self.assertEqual(response.data[0]["coupon_info"]["sale_price"], 30000)
        self.assertEqual(response.data[0]["coupon_info"]["duration"], 7)
        self.assertEqual(response.data[0]["user"], self.user.pk)
        self.assertEqual(response.data[0]["coupon"], self.coupon2.pk)
        self.assertFalse(response.data[0]["status"])

    def test_get_user_coupon_detail(self):
        # 유저가 발급한 쿠폰이 있는 경우 상세정보 불러오기 테스트
        user_coupon = UserCoupon.objects.create(
            user_id=self.user.pk,
            coupon_id=self.coupon.pk,
            expired_at=timezone.now() + timedelta(days=7),
        )
        url = reverse("user-coupon-detail", kwargs={"user_coupon_id": user_coupon.pk})
        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["coupon_info"]["type"], "WELCOME")
        self.assertEqual(response.data["coupon_info"]["content"], "회원가입 축하 쿠폰")
        self.assertEqual(response.data["coupon_info"]["sale_price"], 10000)
        self.assertEqual(response.data["coupon_info"]["duration"], 30)
        self.assertEqual(response.data["user"], self.user.pk)
        self.assertEqual(response.data["coupon"], self.coupon.pk)
        self.assertEqual(response.data["status"], True)

        # 유효하지 않은 유저 쿠폰 번호로 접근하는 경우
        url = reverse("user-coupon-detail", kwargs={"user_coupon_id": 12331311})
        response = self.client.get(url, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # def test_put_user_coupon_detail(self):
    #     # 유저가 발급한 쿠폰이 있는 경우 쿠폰 사용 테스트
    #     user_coupon = UserCoupon.objects.create(
    #         user_id=self.user.pk,
    #         coupon_id=self.coupon.pk,
    #         expired_at=timezone.now() + timedelta(days=30),
    #     )
    #     url = reverse("user-coupon-detail", kwargs={"user_coupon_id": user_coupon.pk})
    #     response = self.client.put(url, headers={"Authorization": f"Bearer {self.token}"})
    #     pdb.set_trace()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data["msg"], "successfully used coupon.")
    #
    #     # 유저가 발급한 쿠폰이 만료된 경우
    #     user_coupon.expired_at = timezone.now()
    #     user_coupon.save()
    #     response = self.client.put(url, headers={"Authorization": f"Bearer {self.token}"})
    #
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data["msg"], "coupon has expired.")
    #
    #     # 이미 사용된 쿠폰인 경우
    #     user_coupon.status = False
    #     user_coupon.save()
    #
    #     response = self.client.put(url, headers={"Authorization": f"Bearer {self.token}"})
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data["msg"], "already used coupon.")
