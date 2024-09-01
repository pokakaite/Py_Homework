from django.urls import path
from .views import *

app_name = 'sales'

urlpatterns = [
    path('', index, name='index')
]