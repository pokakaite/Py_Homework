from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('', index, name='index')
]