from django.db import models

# Create your models here.

class Form2(models.Model):
    CHOICES = [('min','Минимум из трёх'), ('max', 'Максимум из трёх'), ('avg','Среднеарифмитическое из трёх')]
    number_1 = models.IntegerField('Первое число')
    number_2 = models.IntegerField('Второе число')
    number_3 = models.IntegerField('Третье число')
    choice = models.CharField(choices=CHOICES, default=None, max_length=10)