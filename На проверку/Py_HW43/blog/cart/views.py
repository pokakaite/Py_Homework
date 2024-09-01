from django.shortcuts import render
from .models import Cart
from .forms import CartForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

# Create your views here.

def index(request):
    cart = Cart.objects.order_by('order')
    cont = {
        'cart': cart
    }
    return render(request, 'cart/index.html', cont)

class CartCreateView(CreateView):
    model = Cart
    success_url = '/cart/'
    template_name = "cart/create.html"
    form_class = CartForm

class CartDetailView(DetailView):
    model = Cart
    template_name = 'cart/detail.html'
    context_object_name = 'cart'

class CartUpdateView(UpdateView):
    model = Cart
    template_name = "cart/create.html"
    form_class = CartForm
    
class CartDeleteView(DeleteView):
    model = Cart
    success_url = '/cart/'
    template_name = "cart/delete.html"   