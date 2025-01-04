from django.core.management.base import BaseCommand
from books.models import Book
import datetime

class Command(BaseCommand):
    help = 'Seed the database with initial book data'

    def handle(self, *args, **kwargs):
        initial_books = [
            {
                'title': 'Don Quijote de la Mancha',
                'author': 'Miguel de Cervantes',
                'published_date': datetime.datetime(1605, 1, 1),
                'genre': 'Novela',
                'price': 29.99
            },
            {
                'title': 'Cien años de soledad',
                'author': 'Gabriel García Márquez',
                'published_date': datetime.datetime(1967, 1, 1),
                'genre': 'Realismo mágico',
                'price': 24.99
            },
            {
                'title': 'El laberinto de la soledad',
                'author': 'Octavio Paz',
                'published_date': datetime.datetime(1950, 1, 1),
                'genre': 'Ensayo',
                'price': 19.99
            },
            {
                'title': 'Rayuela',
                'author': 'Julio Cortázar',
                'published_date': datetime.datetime(1963, 1, 1),
                'genre': 'Novela',
                'price': 22.99
            },
            {
                'title': 'La casa de los espíritus',
                'author': 'Isabel Allende',
                'published_date': datetime.datetime(1982, 1, 1),
                'genre': 'Novela',
                'price': 27.99
            }
        ]

        for book_data in initial_books:
            Book.objects.create(**book_data)
            self.stdout.write(self.style.SUCCESS(f'Successfully created book: {book_data["title"]}'))