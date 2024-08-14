from django.db import models

# Create your models here.

class Form3(models.Model):
    CHOICES = ('М', 'Мужской'), ('Ж', 'Женский'), ('Н', 'Неважно')
    name = models.CharField('Имя', max_length=25)
    surname = models.CharField('Фамилия', max_length=50)
    age = models.IntegerField('Возраст')
    email = models.EmailField('E-mail')
    gender = models.CharField(choices=CHOICES, default=None, max_length=10)
    address = models.CharField('Адрес', max_length=100)
    agreement = models.Field()