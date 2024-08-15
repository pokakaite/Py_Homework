from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'form1'

urlpatterns = [
    path('', form1, name='form1'),
    path('result', result, name='result')
]