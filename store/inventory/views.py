from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from inventory.models import Product
from api.serializer import ProductSerializer
# Create your views here.

def welcome(request):
    return HttpResponse('Welcome')

@api_view(['GET'])
def api(request):
    
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    
    return Response(serializer.data)