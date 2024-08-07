from django.shortcuts import render, HttpResponseRedirect
from .info import *

def news(request):
        return render(request, 'news.html', info)

def news_smth(request, smth):
    match smth:
        case None:
            return render(request, 'news.html', info)
        case _:
            return HttpResponseRedirect('/news')