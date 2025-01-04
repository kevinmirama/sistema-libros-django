from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated




class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient
from django.conf import settings
from datetime import datetime
from decimal import Decimal

@api_view(['GET'])
def average_price(request, year):
    try:
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client.sistema_libros
        
        # Crear fechas de inicio y fin para el año
        start_date = datetime(year, 1, 1)
        end_date = datetime(year + 1, 1, 1)
        
        pipeline = [
            {
                "$match": {
                    "published_date": {
                        "$gte": start_date,
                        "$lt": end_date
                    }
                }
            },
            {
                "$group": {
                    "_id": {"$year": "$published_date"},
                    "average_price": {"$avg": "$price"}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "year": "$_id",
                    "average_price": {
                        "$convert": {
                            "input": {"$round": ["$average_price", 2]},
                            "to": "double"
                        }
                    }
                }
            }
        ]
        
        result = list(db.books_book.aggregate(pipeline))
        
        if result:
            # Asegurarnos de que el precio sea un float
            response_data = {
                'year': result[0]['year'],
                'average_price': float(result[0]['average_price'])
            }
            return Response(response_data)
        else:
            return Response({
                'year': year,
                'average_price': 0.0
            })
            
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=500)
    finally:
        client.close()
