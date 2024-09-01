from django.db import models
from customer.models import Customer
from salesman.models import Salesman
from products.models import Products

class Cart(models.Model):
        
    order = models.IntegerField('Номер заказа')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman_id = models.ForeignKey(Salesman, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.order
    
    def get_absolute_url(self):
        return f'/cart/{self.id}'