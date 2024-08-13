from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', form2, name='form2'),
    path('result/', result, name='result')
]