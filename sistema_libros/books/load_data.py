import os
import django
from datetime import datetime

# Obtener la ruta del directorio del proyecto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Cambiar al directorio raíz del proyecto
os.chdir(project_root)

# Configurar la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_libros.settings')

# Configurar la ruta para el módulo del proyecto
import sys
sys.path.append(project_root)

django.setup()

from books.models import Book

# Datos de prueba
books_data = [
    {"title": "Book 1", "author": "Author 1", "published_date": "2022-01-01", "genre": "Fiction", "price": 19.99},
    {"title": "Book 2", "author": "Author 2", "published_date": "2022-02-01", "genre": "Non-Fiction", "price": 29.99},
    {"title": "Book 3", "author": "Author 3", "published_date": "2022-03-01", "genre": "Science Fiction", "price": 15.99},
    {"title": "Book 4", "author": "Author 4", "published_date": "2022-04-01", "genre": "Fantasy", "price": 25.99},
    {"title": "Book 5", "author": "Author 5", "published_date": "2022-05-01", "genre": "Mystery", "price": 21.99},
]

for book_data in books_data:
    Book.objects.create(**book_data)

print("Datos de prueba insertados correctamente.")

