from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', index, name='index'),
    path('create', CartCreateView.as_view(), name='create'),
    path('<int:pk>/', CartDetailView.as_view(), name='detail'),
    path('<int:pk>/update', CartUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', CartDeleteView.as_view(), name='delete')
]