import mongoengine
from books.models import  Book
from datetime import datetime


mongoengine.connect('sistema_libros', host='localhost', port=27017)

sample_books = [
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
        'price': 24.99
    }
]

for book_data in sample_books:
    book = Book(**book_data)
    book.save()

print("Datos de muestra creados exitosamente")