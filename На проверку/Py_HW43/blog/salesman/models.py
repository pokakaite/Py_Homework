from django.db import models

# Create your models here.

class Salesman(models.Model):
    name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    number = models.IntegerField('Номер телефона', blank=True)
    email = models.CharField('E-mail', max_length=150, blank=True)
    hiring_date = models.DateTimeField('Дата приёма на работу')
    position = models.CharField('Позиция в фирме', max_length=50, blank=True)

    def __str__(self):
        return self.name