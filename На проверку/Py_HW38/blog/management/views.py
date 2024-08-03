from django.shortcuts import render
from .info import *

def management(request):
    return render(request, 'management.html', info)
