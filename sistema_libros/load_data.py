import os
import django
import sys

# Configura el entorno de Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_libros.settings')
django.setup()

import mongoengine
from books.models import Book
from datetime import datetime

# Desconectard todas las conexiones existentes
mongoengine.disconnect_all()

# Conectar a MongoDB Atlas
mongoengine.connect(
    db='sistema_libros',
    host="mongodb+srv://kevinmirama2:4PNt6F9JXE9q7hUK@cluster0.1buy3.mongodb.net/sistema_libros?retryWrites=true&w=majority&appName=Cluster0"
)

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

try:
    for book_data in sample_books:
        book = Book(**book_data)
        book.save()
    print("Datos de muestra creados exitosamente")
except Exception as e:
    print(f"Error al crear los datos: {e}")