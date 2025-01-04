from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from pymongo import MongoClient
from datetime import datetime
from django.conf import settings


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'], url_path='average-price')
    def average_price(self, request):
        year = request.query_params.get('year')
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]
        pipeline = [
            {"$match": {"published_date": {"$gte": datetime(int(year), 1, 1), "$lt": datetime(int(year) + 1, 1, 1)}}},
            {"$group": {"_id": None, "average_price": {"$avg": "$price"}}}
        ]
        result = list(db.books.aggregate(pipeline))
        avg_price = result[0]['average_price'] if result else None
        return Response({'year': year, 'average_price': avg_price})