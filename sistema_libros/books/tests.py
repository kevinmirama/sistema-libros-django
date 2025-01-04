from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from decimal import Decimal
from .models import Book
from datetime import date

class BookTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_create_book(self):
        data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': '2024-01-01',
            'genre': 'Test Genre',
            'price': '29.99'
        }
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')

    def test_get_average_price(self):
        # Crear algunos libros de prueba
        Book.objects.create(
            title='Book 1',
            author='Author 1',
            published_date='2024-01-01',
            genre='Genre 1',
            price=Decimal('29.99')
        )
        
        response = self.client.get('/api/books/average_price_by_year/?year=2024')
        self.assertEqual(response.status_code, 200)
        self.assertIn('average_price', response.data)





