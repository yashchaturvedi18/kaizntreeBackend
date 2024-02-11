from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Item
from django.contrib.auth.models import User

class ItemAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.item = Item.objects.create(name='Test Item', sku='SKU001', category='Test Category',
                                         tags='tag1, tag2', stock_status='In Stock', available_stock=100)

    def test_item_list_api(self):
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_item_filter_api(self):
        response = self.client.get('/api/items/?category=Test Category')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the filtered item is returned in the response

    def test_user_registration_api(self):
        data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'newpassword'}
        response = self.client.post('/api/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Assert that a new user is created successfully

    def test_user_login_api(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post('/api/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the user is logged in successfully

    def test_item_create_api(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'name': 'New Item', 'sku': 'SKU002', 'category': 'New Category',
                'tags': 'tag1, tag2', 'stock_status': 'In Stock', 'available_stock': 50}
        response = self.client.post('/api/items/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Assert that a new item is created successfully
