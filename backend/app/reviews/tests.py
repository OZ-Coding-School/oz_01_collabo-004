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
            user_id="testuserid",
            password="password123",
            name="testname",
            email="test@example.com",
            phone="01012345678",
        )

        self.product = Product.objects.create(
            name="testname",
            description="testdescription",
            price=1000000,
        )

        self.product2 = Product.objects.create(
            name="testname2",
            description="testdescription2",
            price=2000000,
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
