from django.db import models

# Create your models here.

class Form1(models.Model):
    login = models.CharField('Логин', max_length=50)
    password = models.CharField('Password', max_length=50)