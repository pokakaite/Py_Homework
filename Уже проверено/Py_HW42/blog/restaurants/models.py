from django.db import models

# Create your models here.

class Restaurants(models.Model):
    name = models.CharField('Название', max_length=50)
    cuisine = models.CharField('Кухня', max_length=50)
    address = models.CharField('Адрес', max_length=100)
    web_site = models.CharField('Веб-сайт', max_length=100)
    contacts = models.IntegerField('Номер телефона')