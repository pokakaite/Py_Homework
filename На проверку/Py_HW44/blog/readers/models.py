from django.db import models

# Create your models here.

class Readers(models.Model):
    reader_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.ImageField(unique=True)
    email = models.EmailField(unique=True)
    date = models.DateField