from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'salesman'

urlpatterns = [
    path('', index, name='index'),
    path('add_salesman', AddSalesman.as_view(), name='add_salesman')
]