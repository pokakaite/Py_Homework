from django.db import models

# Create your models here.

class Books(models.Model):
    book_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    publishment = models.CharField(max_length=150)
    in_library = models.BooleanField()


class BooksReaders(models.Model):
    book_id = models.ForeignKey(on_delete=models.CASCADE)