from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializer import ProductSerializer

# Create your views here.
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset
