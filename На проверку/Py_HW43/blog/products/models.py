from django.db import models

# Create your models here.

class Products(models.Model):
    product_id = models.IntegerField()
    name = models.CharField('Название', max_length=50, blank=True)
    description = models.CharField('Описание', max_length=150, blank=True)
    price = models.IntegerField('Цена', blank=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/products/{self.id}'
    