from django.shortcuts import render

# Create your views here.

def form4(request):
    cont = {}
    return render(request, 'form4.html', cont)