from django.shortcuts import render

# Create your views here.

def index(request):
    cont = {}
    return render(request, 'main/index.html', cont)