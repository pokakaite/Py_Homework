from django.shortcuts import render
from .info import *

def news(request):
    return render(request, 'news.html', info)

