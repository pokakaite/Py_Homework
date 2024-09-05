from django.shortcuts import render
from .models import Customers

# Create your views here.

def index(request):
    model = Customers.objects.all()
    cont = {
        'customers': model
    }
    return render(request, 'index.html', cont)