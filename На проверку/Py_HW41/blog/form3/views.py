from django.shortcuts import render

# Create your views here.

def form3(request):
    cont = {}
    return render(request, 'form3.html', cont)