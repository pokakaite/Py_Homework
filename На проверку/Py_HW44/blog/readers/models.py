from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Reader(models.Model):
    name = models.CharField('name', max_length=50, null=False)
    last_name = models.CharField('last_name', max_length=50, null=False)
    number = PhoneNumberField('number', unique=True, null=False, db_index=True)
    email = models.EmailField('email', unique=True, null=False, db_index=True)
    registration_date = models.DateField('registration_date', auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name} ({self.email})'