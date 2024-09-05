from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'customer'

urlpatterns = [
    path('', index, name='index'),
    path('create', CustomerCreateView.as_view(), name='create'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='detail'),
    path('<int:pk>/update', CustomerUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', CustomerDeleteView.as_view(), name='delete')
]