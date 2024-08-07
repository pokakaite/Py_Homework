from django.shortcuts import render


# Create your views here.

def writers(request):
    return render(request, 'writers/writers.html')


def hemingway(request):
    return render(request, 'writers/hemingway.html')


def shakespeare(request):
    cont = {
        'Shakespeare': 'Уи́льям Шекспи́р'
    }
    return render(request, 'writers/writers.html', cont)
