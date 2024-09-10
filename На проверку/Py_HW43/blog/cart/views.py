from django.shortcuts import render
from .models import Cart, CartProducts

# Create your views here.

def index(request):
    cart = Cart.objects.all()
    cart_products = CartProducts.objects.all()
    cont = {
        'cart': cart,
        'cart_products': cart_products
    }
    return render(request, 'cart/index.html', cont)