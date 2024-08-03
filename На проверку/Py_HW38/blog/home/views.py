from django.shortcuts import render
from .info import *

def home(request):
    return render(request, 'home.html', info)
