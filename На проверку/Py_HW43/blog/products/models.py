from django.db import models
from salesman.models import Salesman

# Create your models here.

class Products(models.Model):
    name = models.CharField('Название', max_length=150, blank=True)
    description = models.CharField('Описание', max_length=150, blank=True)
    price = models.IntegerField('Цена', blank=True)
    salesman_id = models.ForeignKey(Salesman, on_delete=models.CASCADE)

    def __str__(self):
        return self.name