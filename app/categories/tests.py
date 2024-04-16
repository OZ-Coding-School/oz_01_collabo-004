from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product

from .models import Category, CategoryUserConnector
from .serializers import ProductConnectorSerializer


class CategoryTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(user_id="testuser", name="testname", password="testpass")
        self.client.force_authenticate(user=self.user)

    def test_get_categories(self) -> None:
        Category.objects.create(name="testcategory1")
        Category.objects.create(name="testcategory2")

        url = reverse("category-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "testcategory1")

    def test_post_category(self) -> None:
        url = reverse("category-list")
        data = {"name": "newcategory"}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(response.data["name"], "newcategory")


class CategoryDetailsTest(APITestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(user_id="testuser", name="testname", password="testpass")
        self.client.force_authenticate(user=self.user)

        self.category = Category.objects.create(name="testcategory")

        self.product = Product.objects.create(name="testproduct", price=1000, description_text="testdescription")

    def test_get_category_details(self) -> None:
        url = reverse("category-detail", kwargs={"category_pk": self.category.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "testcategory")

    def test_put_category_details(self) -> None:
        url = reverse("category-detail", kwargs={"category_pk": self.category.pk})
        updated_data = {"name": "updatedtestcategory"}

        response = self.client.put(url, updated_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "updatedtestcategory")

    def test_delete_category_details(self) -> None:
        url = reverse("category-detail", kwargs={"category_pk": self.category.pk})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=self.category.pk)


class UserCategorySurveyTest(APITestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            user_id="testuser", name="testname", password="testpassword", last_login=None
        )
        self.client.force_authenticate(user=self.user)

        self.category1 = Category.objects.create(name="category1")
        self.category2 = Category.objects.create(name="category2")

    def test_post_category_survey(self) -> None:
        self.assertIsNone(self.user.last_login)
        category_ids = [self.category1.id, self.category2.id]
        data = {"select_category": category_ids}

        url = reverse("user-survey")
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(int(response.data[0]["category"]), self.category1.id)
        self.assertEqual(int(response.data[1]["category"]), self.category2.id)


class UserCategoryListViewTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            user_id="testuser", name="testname", password="testpassword", last_login=None
        )
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name="TestCategory")

        self.connector = CategoryUserConnector.objects.create(category=self.category, user=self.user)

    def test_get_user_list_category(self) -> None:
        url = reverse("user-categories", kwargs={"category_id": self.category.id})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ProductConnectorSerializer([self.connector], many=True).data)

        serialized_data = ProductConnectorSerializer([self.connector], many=True).data
        self.assertEqual(response.data, serialized_data)


class UserCategoryDetailViewTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            user_id="testuser", name="testname", password="testpassword", last_login=None
        )
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name="TestCategory")

        self.connector = CategoryUserConnector.objects.create(category=self.category, user=self.user)

    def test_user_category_details(self) -> None:
        url = reverse("user-detail", kwargs={"category_id": self.category.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(CategoryUserConnector.objects.filter(category=self.category, user=self.user).exists())
        self.assertEqual(response.data, None)

        url = reverse("user-detail", kwargs={"category_id": self.category.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
