from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book
from datetime import datetime

class BookTests(APITestCase):
    def setUp(self):
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': datetime.now(),
            'genre': 'Test Genre',
            'price': 29.99
        }
        self.book = Book.objects.create(**self.book_data)
        
    def test_create_book(self):
        response = self.client.post('/api/books/', self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_average_price_by_year(self):
        response = self.client.get('/api/books/average_price_by_year/?year=2024')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('average_price', response.data)