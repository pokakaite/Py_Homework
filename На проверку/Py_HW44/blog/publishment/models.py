from django.db import models

# Create your models here.

class Publishment(models.Model):
    name = models.CharField('name', max_length=50, unique=True, null=False)

    def __str__(self) -> str:
        return self.name
