from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    number = models.IntegerField('Номер телефона', blank=True)
    email = models.CharField('E-mail', max_length=150, blank=True)