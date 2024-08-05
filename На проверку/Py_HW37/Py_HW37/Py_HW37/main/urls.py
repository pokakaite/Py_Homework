from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.date),
    path('programmers_day/', views.programmers_day),
    path('pythagoras_table/', views.pythagoras_table, name='pythagoras_table'),
    path('2/', views.second_site),
    path('3/', views.third_site),
]