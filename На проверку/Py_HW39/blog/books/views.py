from django.shortcuts import render, HttpResponseRedirect
from .books import *

# Create your views here.

def books(request):
    return render(request, 'books/books.html')

def books_digite(request, digite):
    match digite:
        case 1:
            cont = the_old_man_and_the_sea
        case 2:
            cont = the_sun_also_rises
        case 3:
            cont = hamlet
        case _:
            return HttpResponseRedirect('/books')
    return render(request, 'main/book.html', cont)
            