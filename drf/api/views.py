from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import OrderDetail, Product, Order
from .serializer import ProductSerializer, OrderSerializer, OrderDetailSerializer

# Create your views here.
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        queryset = Order.objects.all()
        return queryset


class OrderDetailViewSet(ModelViewSet):
    serializer_class = OrderDetailSerializer
    
    def get_queryset(self):
        queryset = OrderDetail.objects.all()
        return queryset
