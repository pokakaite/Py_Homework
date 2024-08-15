from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'form3'

urlpatterns = [
    path('', form3, name='form3'),
    path('result/', result, name='result')
]