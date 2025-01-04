from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.authtoken import views as authtoken_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Sistema Libros API",
      default_version='v1',
      description="Documentación de la API de Sistema Libros",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),  # Incluir las URLs de la aplicación books
    path('api-token-auth/', authtoken_views.obtain_auth_token, name='api_token_auth'),  # Endpoint de autenticación
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Documentación Swagger
    path('swagger-json/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-json'),  # JSON del esquema
]


