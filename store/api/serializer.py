from dataclasses import field
from rest_framework import serializers
from inventory.models import *  

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'