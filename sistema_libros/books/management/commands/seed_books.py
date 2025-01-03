from django.core.management.base import BaseCommand
from books.models import Book
from datetime import datetime

class Command(BaseCommand):
    help = 'Load initial books data'

    def handle(self, *args, **kwargs):
        initial_books = [
            {
                'title': 'El Señor de los Anillos',
                'author': 'J.R.R. Tolkien',
                'published_date': datetime(1954, 7, 29),
                'genre': 'Fantasía',
                'price': 25.99
            },
            {
                'title': 'Cien años de soledad',
                'author': 'Gabriel García Márquez',
                'published_date': datetime(1967, 5, 30),
                'genre': 'Realismo mágico',
                'price': 19.99
            },
            {
                'title': '1984',
                'author': 'George Orwell',
                'published_date': datetime(1949, 6, 8),
                'genre': 'Distopía',
                'price': 15.99
            },
            {
                'title': 'Don Quijote de la Mancha',
                'author': 'Miguel de Cervantes',
                'published_date': datetime(1605, 1, 1),
                'genre': 'Novela',
                'price': 22.99
            },
            {
                'title': 'Harry Potter y la piedra filosofal',
                'author': 'J.K. Rowling',
                'published_date': datetime(1997, 6, 26),
                'genre': 'Fantasía',
                'price': 18.99
            }
        ]

        for book_data in initial_books:
            Book.objects.create(**book_data)
            self.stdout.write(self.style.SUCCESS(f'Successfully created book: {book_data["title"]}'))