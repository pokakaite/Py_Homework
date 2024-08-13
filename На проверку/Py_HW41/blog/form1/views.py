from django.shortcuts import render

# Create your views here.

def form1(request):
    cont = {}
    return render(request, 'form1.html', cont)