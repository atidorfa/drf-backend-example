from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=128, default="")
    price = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)


class Order(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    date_time = models.DateTimeField(auto_now_add=True, blank=True)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField() # bugfixed
    product = models.ForeignKey(Product, on_delete=models.CASCADE)