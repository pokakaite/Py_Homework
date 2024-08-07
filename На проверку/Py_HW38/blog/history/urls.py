from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', history, name='history'),
    path('<str:smth>/', history_smth, name='history_smth')
]