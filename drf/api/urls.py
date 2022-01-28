from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, OrderDetailViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('order', OrderViewSet, basename='order')
router.register('orderdetail', OrderDetailViewSet, basename='orderdetail')

urlpatterns = [
    path('', include(router.urls))
]
