from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'form2'

urlpatterns = [
    path('', form2, name='form2'),
    path('result/', result, name='result')
]