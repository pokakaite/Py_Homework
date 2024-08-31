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

class ProductsCreateView(CreateView):
    model = Products
    success_url = '/products/'
    template_name = "products/create.html"
    form_class = ProductsForm

class ProductsDetailView(DetailView):
    model = Products
    template_name = 'products/detail.html'
    context_object_name = 'products'

class ProductsUpdateView(UpdateView):
    model = Products
    template_name = "products/create.html"
    form_class = ProductsForm
    
class ProductsDeleteView(DeleteView):
    model = Products
    success_url = '/products/'
    template_name = "products/delete.html"   