from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cars, name='cars'),
    path('toyota/', toyota, name='toyota'),
    path('honda/', honda, name='honda'),
    path('renault/', renault, name='renault')
]
