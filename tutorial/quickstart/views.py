from rest_framework.viewsets import ModelViewSet     
from .models import Fruit
from .serializers import FruitSerializer 
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.

class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer