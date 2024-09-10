from django.db import models

# Create your models here.

class Salesmen(models.Model):
    POSITIONS = [('Продавец', 'Продавец'), ('Старший продавец', 'Старший продавец'), ('Руководитель отдела продаж', 'Руководитель отдела продаж')]
    salesman_id = models.IntegerField(unique=True)
    name = models.CharField('Имя', max_length=50, blank=True)
    last_name = models.CharField('Фамилия', max_length=50, blank=True)
    number = models.IntegerField('Номер телефона', blank=True, unique=True)
    email = models.EmailField('E-mail', max_length=50, blank=True, unique=True)
    date = models.DateField('Дата приёма на работу')
    position = models.CharField(choices=POSITIONS, default=None, max_length=30, verbose_name='Позиция в фирме')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/salesmen/{self.id}'