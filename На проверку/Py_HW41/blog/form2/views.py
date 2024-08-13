from django.shortcuts import render

# Create your views here.

def form2(request):
    cont = {}
    return render(request, 'form2.html', cont)

def result(request):
    cont = {}
    num_1 = request.GET['input1']
    num_2 = request.GET['input2']
    num_3 = request.GET['input3']

    if num_1 == '' or num_2 == '' or num_3 == '':
        cont.update({'error':'Ошибка. Повторите заново.'})
    
    else:
        numbers = [int(num_1), int(num_2), int(num_3)]
        res = request.GET['radio']
        if res == '':
            cont.update({'error':'Ошибка. Повторите заново.'})
        else:
            if res == 'min':
                cont.update({'res':min(numbers)})
            if res == 'max':
                cont.update({'res':max(numbers)})
            if res == 'avg':
                cont.update({'res':int(sum(numbers)/len(numbers))})
        
    return render(request, 'form2.html', cont)