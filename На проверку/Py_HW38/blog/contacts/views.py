from django.shortcuts import render
from .info import *

def contacts(request):
    return render(request, 'contacts.html', info)