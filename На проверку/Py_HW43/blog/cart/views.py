from django.shortcuts import render
from .models import Cart, CartProducts
from .forms import CartForm, CartProductsForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView


# Create your views here.

def index(request):
    cart = Cart.objects.all()
    cart_products = CartProducts.objects.all()
    cont = {
        'cart': cart,
        'cart_products': cart_products
    }
    return render(request, 'cart/index.html', cont)

# class CartProductsCreateView(CreateView):
#     model = CartProducts
#     success_url = '/cart/'
#     template_name = "cart/create.html"
#     form_class = CartProductsForm

# class CartProductsDetailView(DetailView):
#     model = CartProducts
#     template_name = 'cart/detail.html'
#     context_object_name = 'cart'

# class CartProductsUpdateView(UpdateView):
#     model = CartProducts
#     template_name = "cart/create.html"
#     form_class = CartProductsForm
    
# class CartProductsDeleteView(DeleteView):
#     model = CartProducts
#     success_url = '/cart/'
#     template_name = "cart/delete.html"   