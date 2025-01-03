from mongoengine import Document, StringField, DateTimeField, FloatField
from datetime import datetime

class Book(Document):
    title = StringField(required=True, max_length=200)
    author = StringField(required=True, max_length=100)
    published_date = DateTimeField(required=True)
    genre = StringField(required=True, max_length=50)
    price = FloatField(required=True)
    
    meta = {
        'collection': 'books',
        'db_alias': 'default'
    }