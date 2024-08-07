from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', writers, name='writers'),
    path('Hemingway/', hemingway, name='Hemingway'),
    path('Shakespeare/', shakespeare, name='Shakespeare')
]
