from django.urls import path
from .views import * 

app_name = 'customers'

urlpatterns = [
    path('', index, name='index'),
    path('create', CustomersCreateView.as_view(), name='create'),
    path('<int:pk>/', CustomersDetailView.as_view(), name='detail'),
    path('<int:pk>/update', CustomersUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', CustomersDeleteView.as_view(), name='delete')
]