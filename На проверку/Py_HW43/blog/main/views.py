from django.shortcuts import render

# Create your views here.

def index(request):
    cont = {
        
    }
    return render(request, 'index.html', cont)