from django.shortcuts import render
from .models import Products

# Create your views here.

def index(request):
    model = Products.objects.all()
    cont = {
        'products': model
    }
    return render(request, 'index.html', cont)