from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Product

# Create your tests here.
class TestProductList(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(name='RAM Corsair Vengance 3600 PRO', price='800', stock='20')


    def testproductcreation(self):
        data = {'name': 'RAM KINGSTONE 2600', 'price': '300', 'stock':'10'}
        response = self.client.post("http://127.0.0.1:8000/api/product/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def testproductlist(self):
        response = self.client.get("http://127.0.0.1:8000/api/product/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
