from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

# Create your views here.

def index(request):
    customers = Customer.objects.order_by('name')
    cont = {
        'customers': customers
    }
    return render(request, 'customer/index.html', cont)

class CustomerCreateView(CreateView):
    model = Customer
    success_url = '/customer/'
    template_name = "customer/create.html"
    form_class = CustomerForm

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/detail.html'
    context_object_name = 'customer'

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = "customer/create.html"
    form_class = CustomerForm
    
class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = '/customer/'
    template_name = "customer/delete.html"   
