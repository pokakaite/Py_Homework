from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'customer'

urlpatterns = [
    path('', index, name='index'),
    path('add_customer', AddCustomer.as_view(), name='add_customer')
]