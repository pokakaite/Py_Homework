from django.db import models
from cart.models import Cart

# Create your models here.

class Products(models.Model):
    product_id = models.IntegerField()
    name = models.CharField('Название', max_length=50, blank=True)
    description = models.CharField('Описание', max_length=150, blank=True)
    price = models.IntegerField('Цена', blank=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/products/{self.id}'
    

class CartProducts(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name="products", on_delete=models.CASCADE)
    count = models.IntegerField("Количество товара")
    date = models.DateField()