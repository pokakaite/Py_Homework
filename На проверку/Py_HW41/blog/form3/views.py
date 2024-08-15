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
    cont = {
        'name': request.GET['name'],
        'surname': request.GET['surname'],
        'age': request.GET['age'],
        'email': request.GET['email'],
        'gender': request.GET['gender'],
        'address': request.GET['address'],
        'agreement': request.GET['agreement'],
    }
    return render(request, 'result3.html', cont)
