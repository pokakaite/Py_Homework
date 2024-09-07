from django.shortcuts import render
from .models import Customers
from .forms import CustomersForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

# Create your views here.

def index(request):
    customers = Customers.objects.all()
    cont = {
        'customers': customers
    }
    return render(request, 'customers/index.html', cont)

class CustomersCreateView(CreateView):
    model = Customers
    success_url = '/customers/'
    template_name = "customers/create.html"
    form_class = CustomersForm

class CustomersDetailView(DetailView):
    model = Customers
    template_name = 'customers/detail.html'
    context_object_name = 'customer'

class CustomersUpdateView(UpdateView):
    model = Customers
    template_name = "customers/create.html"
    form_class = CustomersForm
    
class CustomersDeleteView(DeleteView):
    model = Customers
    success_url = '/customers/'
    template_name = "customers/delete.html"   