from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', management, name='management'),
    path('<str:smth>/', management_smth, name='management_smth')
]