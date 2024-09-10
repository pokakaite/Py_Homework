from django.db import models
from salesmen.models import Salesmen
from customers.models import Customers
from products.models import Products


# Create your models here.

class Cart(models.Model):
    cart_id = models.IntegerField()
    salesman_id = models.ForeignKey(Salesmen, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    completed = models.BooleanField('Оформлено?', default=bool)

class CartProducts(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name="products", on_delete=models.CASCADE)
    count = models.IntegerField("Количество товара")
    date = models.DateField()