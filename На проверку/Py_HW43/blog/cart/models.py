from django.db import models
from customer.models import Customer
from salesman.models import Salesman
from products.models import Products

class Cart(models.Model):
    # salesman = models.ForeignKey(Salesman, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # products = models.ForeignKey(Products, on_delete=models.CASCADE)