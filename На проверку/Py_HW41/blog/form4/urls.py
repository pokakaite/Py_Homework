from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', form4, name='form4')
]