from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField('name', max_length=30, null=False)
    last_name = models.CharField('last_name', max_length=30, null=False)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'
    
    @property
    def short_name(self):
        return f'{self.last_name} {self.name[:1]}.'