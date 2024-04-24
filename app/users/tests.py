from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserTestCase(APITestCase):
    def test_회원가입_정보가_유효한_경우_테스트(self) -> None:
        url = reverse("signup")
        data = {
            "user_id": "testuserid123",
            "email": "test@example.com",
            "nickname": "testnickname",
            "name": "name",
            "phone": "01011110101",
            "password": "password1234",
            "password2": "password1234",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user(self) -> None:
        user_id = "testuserid"
        password = "password1234"
        name = "testname"
        email = "test@example.com"
        phone = "01012345678"

        user = get_user_model().objects.create_user(
            user_id=user_id, password=password, name=name, email=email, phone=phone
        )

        self.assertEqual(user.user_id, user_id)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self) -> None:
        user_id = "testsuperuserid"
        password = "password1234"
        name = "test2name"
        email = "test2@example.com"
        phone = "01012345648"

        user = get_user_model().objects.create_superuser(
            user_id=user_id, password=password, name=name, email=email, phone=phone
        )

        self.assertEqual(user.user_id, user_id)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_superuser)

    def test_유저의_정보가_일치할_때_로그인_테스트(self) -> None:
        get_user_model().objects.create_user(
            user_id="testuserid",
            password="testpassword123",
            name="testname",
            email="test@example.com",
            phone="01012345678",
        )
        url = reverse("jwt_login")
        data = {"user_id": "testuserid", "password": "testpassword123"}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("AUT_REF", response.cookies)
        self.assertIn("access", response.data)

    def test_유저의_정보가_일치하지_않을_때_로그인_테스트(self) -> None:
        data = {"user_id": "invalid", "password": "invalid"}
        url = reverse("jwt_login")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_로그인_유저의_로그아웃_테스트(self) -> None:
        user = get_user_model().objects.create_user(
            user_id="testuserid",
            password="testpassword123",
            name="testname",
            email="test@example.com",
            phone="01012345678",
        )

        refresh_token = RefreshToken.for_user(user)

        self.client.cookies["AUT_REF"] = str(refresh_token)
        access_token = refresh_token.access_token  # type: ignore
        url = reverse("jwt_logout")
        response = self.client.post(url, headers={"Authorization": f"Bearer {access_token}"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn(str(refresh_token), response.cookies)


class UserDetailViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            user_id="testuserid",
            password="testpassword123",
            name="testname",
            email="test@example.com",
            phone="01012345678",
        )

    def test_get_user_detail(self) -> None:
        url = reverse("user_detail")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user_id"], self.user.user_id)
        self.assertEqual(response.data["name"], self.user.name)
        self.assertEqual(response.data["email"], self.user.email)
        self.assertEqual(response.data["phone"], self.user.phone)

    def test_put_user_detail(self) -> None:
        url = reverse("user_detail")
        data = {"nickname": "Updated NickName", "email": "updated@example.com", "phone": "01234567890"}
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nickname"], self.user.nickname)
        self.assertEqual(response.data["email"], data.get("email"))
        self.assertEqual(response.data["phone"], data.get("phone"))

    def test_delete_user_detail(self) -> None:
        url = reverse("user_detail")
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(User.objects.get(user_id=self.user.user_id).is_active)
