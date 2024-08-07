from django.shortcuts import render, HttpResponseRedirect
from .info import *

def facts(request):
    return render(request, 'facts.html', info)


def facts_smth(request, smth):
    match smth:
        case None:
            return render(request, 'facts.html', info)
        case _:
            return HttpResponseRedirect('/facts')