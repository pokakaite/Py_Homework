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

class AddCustomer(CreateView):
    model = Customer
    success_url = '/customer/'
    template_name = "customer/add_customer.html"
    form_class = CustomerForm