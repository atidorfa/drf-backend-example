from itertools import product
from django.shortcuts import render
from django.db import IntegrityError, transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
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

    def create(self, request, *args, **kwars):
        orderdetail_data = request.data

        product_data = Product.objects.get(pk=orderdetail_data['product'])
        quantity_data = int(orderdetail_data['quantity'])

        if product_data.stock >= quantity_data:
            try:
                with transaction.atomic():    
                    order_detail = OrderDetail.objects.create(order=Order.objects.get(pk=orderdetail_data['order']), quantity=quantity_data, product=product_data)
                    product_data.stock = product_data.stock - quantity_data
                    
                    order_detail.save()
                    product_data.save()

                    serializer = OrderDetailSerializer(order_detail)
                    response = Response(serializer.data)
            except IntegrityError:
                # Transaction failed - return a response notifying the client
                return Response({'message': 'Failed to complete order detail, please try again!'})

        else:
            response = Response({'message': 'OUT OF STOCK'})

        return response