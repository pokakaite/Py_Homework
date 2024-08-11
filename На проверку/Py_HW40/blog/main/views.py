from django.shortcuts import render
from .views import *

# Create your views here.

def main(request):
    return render(request, 'menu.html')