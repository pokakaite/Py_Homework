from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news, name='news'),
    path('<str:smth>/', news_smth, name='news_smth')
]