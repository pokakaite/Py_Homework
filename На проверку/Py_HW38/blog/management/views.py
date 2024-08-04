from django.shortcuts import render, HttpResponseRedirect
from .info import *

def management(request):
    return render(request, 'management.html', info)


def management_smth(request, smth):
    match smth:
        case None:
            return render(request, 'management.html', info)
        case _:
            return HttpResponseRedirect('/management')