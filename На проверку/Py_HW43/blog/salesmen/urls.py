from django.urls import path
from .views import * 

app_name = 'salesmen'

urlpatterns = [
    path('', index, name='index')
]