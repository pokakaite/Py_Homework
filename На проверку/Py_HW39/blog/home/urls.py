from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('choose/', choose, name='choose'),
    path('books_list/', books_list, name='books_list')
]
