from django.urls import path
from .views import * 

app_name = 'salesmen'

urlpatterns = [
    path('', index, name='index'),
    path('create', SalesmenCreateView.as_view(), name='create'),
    path('<int:pk>/', SalesmenDetailView.as_view(), name='detail'),
    path('<int:pk>/update', SalesmenUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', SalesmenDeleteView.as_view(), name='delete')
]