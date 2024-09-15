from django.db import models
from readers.models import Readers

# Create your models here.

class Books(models.Model):
    book_id = models.IntegerField(unique=True, primary_key=True, null=False)
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    publishment = models.CharField(max_length=150)
    in_library = models.BooleanField(default=bool)
    reader_id = models.ForeignKey(Readers, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name