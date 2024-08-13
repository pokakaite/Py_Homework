from django.shortcuts import render

# Create your views here.

def home(request):
    cont = {
        'form1': "Задание 1. Первая форма",
        'form2': "Задание 2. Вторая форма",
        'form3': "Задание 3. Третья форма",
        'form4': "Задание 4. Четвёртая форма"
    }
    return render(request, 'home.html', cont)