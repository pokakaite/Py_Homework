from django.shortcuts import render
import datetime

# Create your views here.

def weekday(request):
    week = {
        '0': 'Понедельник',
        '1': 'Вторник',
        '2': 'Среда',
        '3': 'Четверг',
        '4': 'Пятница',
        '5': 'Суббота',
        '6': 'Воскресенье'
    }
    date = datetime.datetime.now()
    weekday = week[str(date.weekday())]
    match weekday:
        case 'Понедельник':
            color = 'red'
        case 'Вторник':
            color = 'orange'
        case 'Среда':
            color = 'yellow'
        case 'Четверг':
            color = 'green'
        case 'Пятница':
            color = 'light-blue'
        case 'Суббота':
            color = 'blue'
        case 'Воскресенье':
            color = 'purple'

    cont = {
        'weekday': weekday,
        'color': color
    }
    return render(request, 'weekday/weekday.html', cont)