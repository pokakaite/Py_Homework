from django.db import models
from cart.models import Cart


# Create your models here.

class Sales(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    date = models.DateField('Дата продажи')
    summ = models.IntegerField('Сумма продажи')