from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', form1, name='form1')
]