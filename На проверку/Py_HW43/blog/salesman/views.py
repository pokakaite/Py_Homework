from django.shortcuts import render
from .models import Salesman
from .forms import SalesmanForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

# Create your views here.

def index(request):
    salesmen = Salesman.objects.order_by('name')
    cont = {
        'salesmen': salesmen
    }
    return render(request, 'salesman/index.html', cont)

class AddSalesman(CreateView):
    model = Salesman
    success_url = '/salesman/'
    template_name = "salesman/add_salesman.html"
    form_class = SalesmanForm