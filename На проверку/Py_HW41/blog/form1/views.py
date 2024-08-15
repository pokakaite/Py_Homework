from django.shortcuts import render
from .forms import Form1_Form

access = {
    'user_login':'pokakaite',
    'user_password':'Poka12345',
    'admin_login':'admin',
    'admin_password':'Admin12345',
}

# Create your views here.

def form1(request):
    form = Form1_Form
    cont = access
    cont.update({'form':form})
    return render(request, 'form1.html', cont)

def result(request):
    login = request.GET['login']
    password = request.GET['password']
    cont = {}
    if login == 'pokakaite': 
        if password == 'Poka12345':
            cont.update({'success_user':'Вы успешно зашли как пользователь'})
        else:
            cont.update({'success_user':'Неправильно введён пароль'})
    elif login == 'admin':
        if password == 'Admin12345':
            cont.update({'success_admin':'Вы успешно зашли как админ'})
        else:
            cont.update({'success_admin':'Неправильно введён пароль'})
    else:
        cont.update({'error':'Такого пользователя/админа не существует. Попробуйте снова.'})
        
    return render(request, 'result1.html', cont)
