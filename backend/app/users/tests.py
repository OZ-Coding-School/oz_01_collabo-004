from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import User


class UserTestCase(APITestCase):
    def test_signup_user(self):
        url = reverse('register')
        data = {'email': 'test@example.com', 'name': 'name', 'password': 'password1234', 'password2': 'password1234'}
        data2 = {'email': 'test2@example.com', 'name': 'name2', 'password': 'password1234', 'password2': 'password123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        response2 = self.client.post(url, data2)
        self.assertEqual(response2.status_code, 400)

    def test_create_user(self):
        user_id = 'testuserid'
        password = 'password1234'
        name = 'testname'
        email = 'test@example.com'
        phone = '01012345678'

        user = get_user_model().objects.create_user(
            user_id=user_id,
            password=password,
            name=name,
            email=email,
            phone=phone
        )

        self.assertEqual(user.user_id, user_id)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user_id = 'testsuperuserid'
        password = 'password1234'
        name = 'test2name'
        email = 'test2@example.com'
        phone = '01012345648'

        user = get_user_model().objects.create_superuser(
            user_id=user_id,
            password=password,
            name=name,
            email=email,
            phone=phone
        )

        self.assertEqual(user.user_id, user_id)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_superuser)