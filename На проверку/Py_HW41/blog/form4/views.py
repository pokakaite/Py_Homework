from django.shortcuts import render
from .forms import Form4_Form
import datetime

week = {
    '0': 'Понедельник',
    '1': 'Вторник',
    '2': 'Среда',
    '3': 'Четверг',
    '4': 'Пятница',
    '5': 'Суббота',
    '6': 'Воскресенье'
    }

# Create your views here.

def form4(request):
    form = Form4_Form
    cont = {
        'form': form
    }
    return render(request, 'form4.html', cont)

def result(request):
    form = Form4_Form
    cont = {
        'form': form
    }
    year = int(request.GET['year'])
    res = datetime.datetime(year, 9, 13)
    weekday = week[str(res.weekday())]
    cont.update({'res': weekday})
    return render(request, 'form4.html', cont)