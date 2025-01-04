# urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from rest_framework import permissions
from rest_framework.authtoken import views as authtoken_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Sistema Libros API",
      default_version='v1',
      description="Documentación de la API de Sistema Libros",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@sistemalibros.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Redirección de la raíz a Swagger
    path('', RedirectView.as_view(url='/swagger/', permanent=True)),
    
    # Admin y API URLs
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    
    # Autenticación
    path('api-token-auth/', authtoken_views.obtain_auth_token, name='api_token_auth'),
    
    # Swagger URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

