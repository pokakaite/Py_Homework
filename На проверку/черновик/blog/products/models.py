from django.db import models
from salesman.models import Salesman

# Create your models here.

class Products(models.Model):
    name = models.CharField('Название', max_length=150, blank=True)
    description = models.CharField('Описание', max_length=150, blank=True)
    price = models.IntegerField('Цена', blank=True)
    salesman_id = models.ForeignKey(Salesman, on_delete=models.CASCADE)
    # sales = models.ManyToManyField(Sales)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/products/{self.id}'
    

# class Cart(models.Model):
#     salesman = models.ForeignKey
#     customer = rfgth
#     completed = models.BooleanField('Оформлено?', default=bool)
    

# class CartProducts(models.Model):
#     products = models.ForeignKey(Products, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, related_name="products", on_delete=models.CASCADE)
#     count = models.IntegerField("Количество товара", default=lambda:1)
#     date = ...