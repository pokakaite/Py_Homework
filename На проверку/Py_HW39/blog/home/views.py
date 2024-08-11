from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def choose(request):
    return render(request, 'home/choose.html')

def books_list(request):
    cont = {}
    writer = request.GET['writer']
    year = request.GET['year']
    if writer == 'Hemingway':
        writer = 'Эрне́ст Ми́ллер Хемингуэ́й'
    if writer == 'Shakespeare':
        writer = 'Уи́льям Шекспи́р'
    cont.update({'writer':writer})
    cont.update({'year':year})
    if writer == 'Эрне́ст Ми́ллер Хемингуэ́й' and (int(year) < 1926 or int(year) > 1927):
        return HttpResponseRedirect('/writers/Hemingway')
    if writer == 'Уи́льям Шекспи́р' and (int(year) < 1601 or int(year) > 1602):
        return HttpResponseRedirect('/writers/Shakespeare')
    else:
        return render(request, 'home/books_list.html', cont)