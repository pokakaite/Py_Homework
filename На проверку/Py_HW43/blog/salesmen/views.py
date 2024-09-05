from django.shortcuts import render
from .models import Salesmen

# Create your views here.

def index(request):
    model = Salesmen.objects.order_by('salesman_id')
    cont = {
        'model': model
    }
    return render(request, 'index.html', cont)