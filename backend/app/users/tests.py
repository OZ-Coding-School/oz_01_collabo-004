# from rest_framework.test import APITestCase
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from .models import User
# from rest_framework import status


# class UserTestCase(APITestCase):
#     def test_signup_user(self):
#         url = reverse('signup')
#         data = {'email': 'test@example.com', 'name': 'name', 'password': 'password1234', 'password2': 'password1234'}
#         data2 = {'email': 'test2@example.com', 'name': 'name2', 'password': 'password1234', 'password2': 'password123'}
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         response2 = self.client.post(url, data2)
#         self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_user(self):
#         user_id = 'testuserid'
#         password = 'password1234'
#         name = 'testname'
#         email = 'test@example.com'
#         phone = '01012345678'

#         user = get_user_model().objects.create_user(
#             user_id=user_id,
#             password=password,
#             name=name,
#             email=email,
#             phone=phone
#         )

#         self.assertEqual(user.user_id, user_id)
#         self.assertTrue(user.check_password(password))
#         self.assertFalse(user.is_superuser)

#     def test_create_superuser(self):
#         user_id = 'testsuperuserid'
#         password = 'password1234'
#         name = 'test2name'
#         email = 'test2@example.com'
#         phone = '01012345648'

#         user = get_user_model().objects.create_superuser(
#             user_id=user_id,
#             password=password,
#             name=name,
#             email=email,
#             phone=phone
#         )

#         self.assertEqual(user.user_id, user_id)
#         self.assertTrue(user.check_password(password))
#         self.assertTrue(user.is_superuser)

#     def test_login_user(self):
#         user = get_user_model().objects.create_user(
#             user_id='testuserid',
#             password='testpassword123',
#             name='testname',
#             email='test@example.com',
#             phone='01012345678'
#             )
#         url = reverse('jwt_login')
#         data = {'user_id': 'testuserid', 'password': 'testpassword123'}
#         response = self.client.post(url, data)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('AUT_ACC', response.cookies)
#         self.assertIn('AUT_REF', response.cookies)

#         data2 = {'user_id': 'invalid', 'password': 'invalid'}
#         response2 = self.client.post(url, data2)
#         self.assertEqual(response2.status_code, status.HTTP_401_UNAUTHORIZED)

# class UserDetailViewTestCase(APITestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             user_id='testuserid',
#             password='testpassword123',
#             name='testname',
#             email='test@example.com',
#             phone='01012345678'
#             )

#     def test_get_user_detail(self):
#         url = reverse('user_detail')
#         self.client.force_authenticate(user=self.user)
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_put_user_detail(self):
#         url = reverse('user_detail')
#         data = {
#             'name': 'Updated Name',
#             'email': 'updated@example.com',
#             'phone': '01234567890'
#         }
#         self.client.force_authenticate(user=self.user)
#         response = self.client.put(url, data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_delete_user_detail(self):
#         url = reverse('user_detail')
#         self.client.force_authenticate(user=self.user)
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
