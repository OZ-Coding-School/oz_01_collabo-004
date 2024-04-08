from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from .models import Category


class CategoryTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(user_id="testuser", name="testname", password="testpass")
        self.client.force_authenticate(user=self.user)

    def test_get_categories(self):
        Category.objects.create(name="testcategory1")
        Category.objects.create(name="testcategory2")

        url = reverse("category-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "testcategory1")

    def test_post_category(self):
        url = reverse("category-list")
        data = {"name": "newcategory"}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)


class CategoryDetailsTest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(user_id="testuser", name="testname", password="testpass")
        self.client.force_authenticate(user=self.user)

        self.category = Category.objects.create(name="testcategory")

    def test_get_category_details(self):
        url = reverse("category-detail", kwargs={"category_pk": self.category.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "testcategory")

    def test_put_category_details(self):
        url = reverse("category-detail", kwargs={"category_pk": self.category.pk})
        updated_data = {"name": "updatedtestcategory"}

        response = self.client.put(url, updated_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "updatedtestcategory")

    def test_delete_category_details(self):
        url = reverse("category-detail", kwargs={"category_pk": self.category.pk})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=self.category.pk)


class UserCategorySurveyTest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            user_id="testuser", name="testname", password="testpassword", last_login=None
        )
        self.client.force_authenticate(user=self.user)

        self.category1 = Category.objects.create(name="category1")
        self.category2 = Category.objects.create(name="category2")

    def test_post_category_survey(self):
        self.assertIsNone(self.user.last_login)
        category_ids = [self.category1.id, self.category2.id]

        data = {"select_category": category_ids}
        url = reverse("user-survey")
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
