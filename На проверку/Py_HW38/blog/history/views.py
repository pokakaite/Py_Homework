from django.shortcuts import render
from .info import *

def history(request):
    return render(request, 'history.html', info)
