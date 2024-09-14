from django.urls import path
from .views import *

app_name = 'readers'

urlpatterns = [
    path('', index, name='index')
]
