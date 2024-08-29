from django.db import models
from salesman.models import Salesman



# Create your models here.

class Products(models.Model):
    name = models.CharField('Название', max_length=150, blank=True, null=True)
    description = models.CharField('Описание', max_length=150, blank=True, null=True)
    salesman = models.ForeignKey(Salesman, on_delete=models.CASCADE)

