from django.shortcuts import render, HttpResponseRedirect
from .info import *

def contacts(request):
    return render(request, 'contacts.html', info)


def contacts_smth(request, smth):
    match smth:
        case None:
            return render(request, 'contacts.html', info)
        case _:
            return HttpResponseRedirect('/contacts')