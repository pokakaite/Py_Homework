from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', books, name='books'),
    path('<int:digite>/', books_digite, name='books_digite')
]
