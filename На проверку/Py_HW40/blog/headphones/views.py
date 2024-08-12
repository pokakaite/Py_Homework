from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

def headphones(request):
    return render(request, 'headphones.html')

def result(request):
    cont = {}
    model = request.GET['model']
    cont.update({'model':model})
    return render(request, 'headphones.html', cont)
