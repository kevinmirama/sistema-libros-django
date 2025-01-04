# books/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
import datetime
from bson import ObjectId

class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Aquí deberías configurar la autenticación para tus pruebas
        
    def test_create_book(self):
        data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': '2024-01-01T00:00:00Z',
            'genre': 'Test Genre',
            'price': '29.99'
        }
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_average_price_by_year(self):
        response = self.client.get('/api/books/average_price_by_year/?year=2024')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('average_price' in response.data)




