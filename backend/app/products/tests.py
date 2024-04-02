from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Product
from .serializers import ProductSerializer

class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.products_url = reverse('product-list')
        self.product1 = Product.objects.create(name='상품1', description='상품1 설명', price=10000)
        self.product2 = Product.objects.create(name='상품2', description='상품2 설명', price=20000)

    def test_get_product_list(self):
        response = self.client.get(self.products_url)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_product(self):
        data = {'name': '새로운 상품', 'description': '새로운 상품 설명', 'price': 30000}
        response = self.client.post(self.products_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 3)

    def test_get_product_detail(self):
        product_url = reverse('product-detail', args=[self.product1.id])
        response = self.client.get(product_url)
        serializer = ProductSerializer(self.product1)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_product(self):
        product_url = reverse('product-detail', args=[self.product1.id])
        data = {'name': '수정된 상품', 'description': '수정된 상품 설명', 'price': 15000}
        response = self.client.put(product_url, data, format='json')
        updated_product = Product.objects.get(id=self.product1.id)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_product.name, '수정된 상품')

    def test_delete_product(self):
        product_url = reverse('product-detail', args=[self.product1.id])
        response = self.client.delete(product_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 1)
