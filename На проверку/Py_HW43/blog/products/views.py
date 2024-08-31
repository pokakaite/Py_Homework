from django.shortcuts import render
from .models import Products
from .forms import ProductsForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

# Create your views here.

def index(request):
    products = Products.objects.order_by('name')
    cont = {
        'products': products
    }
    return render(request, 'products/index.html', cont)

class AddProduct(CreateView):
    model = Products
    success_url = '/products/'
    template_name = "products/add_product.html"
    form_class = ProductsForm