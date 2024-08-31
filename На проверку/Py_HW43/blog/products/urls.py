from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('create', ProductsCreateView.as_view(), name='create'),
    path('<int:pk>/', ProductsDetailView.as_view(), name='detail'),
    path('<int:pk>/update', ProductsUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ProductsDeleteView.as_view(), name='delete')
]