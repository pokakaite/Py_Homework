from django.db import models
from salesmen.models import Salesmen
from customers.models import Customers

# Create your models here.

class Cart(models.Model):
    salesman_id = models.ForeignKey(Salesmen, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    completed = models.BooleanField('Оформлено?', default=bool)