from .models import Fruit
from rest_framework import serializers


class FruitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:        
        model = Fruit   
        fields = ('name', 'price')  