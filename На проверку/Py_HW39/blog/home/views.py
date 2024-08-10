from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def choose(request):
    return render(request, 'home/choose.html')

def books_list(request):
    cont = {}
    writer = request.GET['writer']
    year = request.GET['year']
    cont.update({'writer':writer})
    cont.update({'year':year})
    return render(request, 'home/books_list.html', cont)