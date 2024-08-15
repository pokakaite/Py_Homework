from django.shortcuts import render
from .forms import Form3_Form

# Create your views here.

def form3(request):
    form = Form3_Form
    cont = {
        'form': form
    }
    return render(request, 'form3.html', cont)

def result(request):
    cont = {}
    return render(request, 'form3.html', cont)
