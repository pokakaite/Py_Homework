from django.shortcuts import render, HttpResponseRedirect
from .books import *


# Create your views here.

def writers(request):
    return render(request, 'writers/writers.html')

def hemingway(request):
    return render(request, 'writers/hemingway.html')

def shakespeare(request):
    return render(request, 'writers/shakespeare.html')

def smth(request, smth):
    match smth:
        case 'Hemingway':
            return render(request, 'writers/hemingway.html')
        case 'Skakespeare':
            return render(request, 'writers/shakespeare.html')
        case _:
            return HttpResponseRedirect('/writers')

def hemingway_book(request, book):
    match book:
        case 'The_Old_Man_and_the_Sea':
            cont = the_old_man_and_the_sea
            return render(request, 'main/book.html', cont)
        case 'The_Sun_Also_Rises':
            cont = the_sun_also_rises
            return render(request, 'main/book.html', cont)
        case _:
            return HttpResponseRedirect('/Hemingway')

def shakespeare_book(request, book):
    match book:
        case 'Hamlet':
            cont = hamlet
            return render(request, 'main/book.html', cont)
        case _:
            return HttpResponseRedirect('/Shakespeare')