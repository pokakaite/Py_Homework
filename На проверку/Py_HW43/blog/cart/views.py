from django.shortcuts import render
from .models import Cart

# Create your views here.

def index(request):
    model = Cart.objects.all()
    cont = {
        'cart': model
    }
    return render(request, 'index.html', cont)