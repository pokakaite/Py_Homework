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

class SalesmanCreateView(CreateView):
    model = Salesman
    success_url = '/salesman/'
    template_name = "salesman/create.html"
    form_class = SalesmanForm

class SalesmanDetailView(DetailView):
    model = Salesman
    template_name = 'salesman/detail.html'
    context_object_name = 'salesman'

class SalesmanUpdateView(UpdateView):
    model = Salesman
    template_name = "salesman/create.html"
    form_class = SalesmanForm
    
class SalesmanDeleteView(DeleteView):
    model = Salesman
    success_url = '/salesman/'
    template_name = "salesman/delete.html"   