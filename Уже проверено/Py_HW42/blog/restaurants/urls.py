from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'restaurants'

urlpatterns = [
    path('', index, name='index'),
    path('create/', CreateRestaurant.as_view(), name='create'),
    path('show/<int:pk>/', ShowRestaurants.as_view(), name='show'),
    path('<int:pk>/delete', DeleteRestaurant.as_view(), name='delete'),
    path('<int:pk>/edit', EditRestaurant.as_view(), name='edit'),
    path('<int:pk>/search', SearchRestaurant.as_view(), name='search'),
]
