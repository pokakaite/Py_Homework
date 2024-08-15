from django.shortcuts import render
from .forms import Form2_Form

# Create your views here.

def form2(request):
    form = Form2_Form
    cont = {
        'form': form
    }
    return render(request, 'form2.html', cont)

def result(request):
    form = Form2_Form
    cont = {
        'form': form
    }
    num_1 = request.GET['number_1']
    num_2 = request.GET['number_2']
    num_3 = request.GET['number_3']
    
    numbers = [int(num_1), int(num_2), int(num_3)]
    res = request.GET['choice']

    if res == 'min':
        cont.update({'res':min(numbers)})
    if res == 'max':
        cont.update({'res':max(numbers)})
    if res == 'avg':
        cont.update({'res':int(sum(numbers)/len(numbers))})
    
    return render(request, 'form2.html', cont)