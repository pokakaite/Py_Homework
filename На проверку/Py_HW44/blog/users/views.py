from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            messages.success(request, f'Регистрация {username} прошла успешно')
            form.save()
            redirect('login/')
        else:
            messages.warning(request, 'Неправильно')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {
        'form': form
    })
