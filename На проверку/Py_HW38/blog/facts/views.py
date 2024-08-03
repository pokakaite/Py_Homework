from django.shortcuts import render
from .info import *

def facts(request):
    return render(request, 'facts.html', info)