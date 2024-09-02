from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField()
    name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    number = models.IntegerField('Номер телефона', blank=True, unique=True)
    email = models.EmailField('E-mail', max_length=150, blank=True, unique=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/customer/{self.id}'