from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'salesman'

urlpatterns = [
    path('', index, name='index')
]