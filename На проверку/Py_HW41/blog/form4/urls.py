from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'form4'

urlpatterns = [
    path('', form4, name='form4')
]