from django.shortcuts import render, HttpResponseRedirect
from .info import *

def history(request):
    return render(request, 'history.html', info)

def history_smth(request, smth):
    match smth:
        case None:
            return render(request, 'history.html', info)
        case 'people':
            cont = info.copy()
            cont.update({smth:'Известные личности города'})
            return render(request, 'history.html', cont)
        case 'photos':
            cont = info.copy()
            cont.update({smth:'Исторические фотографии города'})
            return render(request, 'history.html', cont)
        case _:
            return HttpResponseRedirect('/history')