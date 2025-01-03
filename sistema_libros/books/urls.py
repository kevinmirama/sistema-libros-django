from rest_framework_mongoengine import routers
from django.urls import path, include
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', viewset=BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]