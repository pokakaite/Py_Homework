from django.shortcuts import render
from django.http import HttpResponse
import datetime

def date(request):
    current_date = datetime.datetime.now()
    return HttpResponse(f'<h1>Текущий день и время - {current_date}<h1>')

def programmers_day(request):
    return HttpResponse(f'<h1>День программиста - {(datetime.timedelta(256) + datetime.datetime(2024, 1, 1))}<h1>')

def pythagoras_table(request):
    return render(request, 'index.html')

def second_site(request):
    return render(request, 'index2.html')

def third_site(request):
    return render(request, 'index3.html')