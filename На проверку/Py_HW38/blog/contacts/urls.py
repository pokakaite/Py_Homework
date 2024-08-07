from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contacts, name='contacts'),
    path('<str:smth>/', contacts_smth, name='contacts_smth')
]