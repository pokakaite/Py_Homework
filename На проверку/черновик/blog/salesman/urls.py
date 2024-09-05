from django.urls import path
from .views import *

app_name = 'salesman'

urlpatterns = [
    path('', index, name='index'),
    path('create', SalesmanCreateView.as_view(), name='create'),
    path('<int:pk>/', SalesmanDetailView.as_view(), name='detail'),
    path('<int:pk>/update', SalesmanUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', SalesmanDeleteView.as_view(), name='delete')
]