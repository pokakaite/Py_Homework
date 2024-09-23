from django.db import models
from readers.models import Reader
from authors.models import Author
from genres.models import Genre
from publishment.models import Publishment

# Create your models here.

class Book(models.Model):
    name = models.CharField('name', max_length=30, null=False)
    author = models.ForeignKey(Author, null=False, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, null=False, on_delete=models.CASCADE)
    publishment = models.ForeignKey(Publishment, null=False, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, null=True, blank=True, on_delete=models.CASCADE)
    year = models.IntegerField('year', null=False)

    def __str__(self) -> str:
        return f'{self.author.short_name} {self.name} - {self.publishment}, {self.year}'

from django.db import models
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'genre']

# ViewSets define the view behavior.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

