from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', facts, name='facts'),
    path('<str:smth>/', facts_smth, name='facts_smth')
]