from django.shortcuts import render

# Create your views here.

def writers(request):
    return render(request, 'writers/writers.html')

def hemingway(request):
    cont = {
        'hemingway':'Эрне́ст Ми́ллер Хемингуэ́й'
    }
    return render(request, 'writers/writers.html', cont)
        
def shakespeare(request):
    cont = {
        'shakespeare':'Уи́льям Шекспи́р'
    }
    return render(request, 'writers/writers.html', cont)