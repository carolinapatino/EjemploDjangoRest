from django.urls import include, path
from rest_framework import routers     
from quickstart import views

router = routers.DefaultRouter()  #Api asistente
router.register(r'fruit', views.FruitViewSet)  # Especifique la ruta y procese la solicitud de solicitud.

urlpatterns = [
    path('api/v1/', include(router.urls)),  # Determinar URL
]