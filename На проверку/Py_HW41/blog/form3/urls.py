from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', form3, name='form3'),
    path('result/', result, name='result')
]