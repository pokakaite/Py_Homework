from django.shortcuts import render

# Create your views here.

def cars(request):
    return render(request, 'cars/cars.html')

def toyota(request):
    cont = {
        'car': 'Тойота'
    }
    return render(request, 'cars/cars.html', cont)

def honda(request):
    cont = {
        'car': 'Хонда'
    }
    return render(request, 'cars/cars.html', cont)

def renault(request):
    cont = {
        'car': 'Рено'
    }
    return render(request, 'cars/cars.html', cont)
