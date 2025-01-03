from rest_framework_mongoengine import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from datetime import datetime

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return Book.objects.all()
    
    @action(detail=False, methods=['get'])
    def average_price_by_year(self, request):
        year = request.query_params.get('year')
        if not year:
            return Response({'error': 'Year parameter is required'}, status=400)
            
        start_date = datetime(int(year), 1, 1)
        end_date = datetime(int(year), 12, 31)
        
        pipeline = [
            {
                '$match': {
                    'published_date': {
                        '$gte': start_date,
                        '$lte': end_date
                    }
                }
            },
            {
                '$group': {
                    '_id': None,
                    'average_price': {'$avg': '$price'}
                }
            }
        ]
        
        result = Book.objects.aggregate(pipeline)
        result_list = list(result)
        
        if result_list:
            return Response({'average_price': result_list[0]['average_price']})
        return Response({'average_price': 0})