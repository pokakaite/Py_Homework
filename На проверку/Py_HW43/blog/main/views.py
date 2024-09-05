from django.shortcuts import render

# Create your views here.

def index(request):
    cont = {
        'show_customers': 'Отобразить информацию о покупателях',
        'show_salesmen': 'Отобразить информацию о продавцах',
        'show_products': 'Отобразить информацию о товарах',
        'show_cart': 'Отобразить информацию о продажах'
    }
    return render(request, 'index.html', cont)