from django.shortcuts import render
from .models import Salesmen
from .forms import SalesmenForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

# Create your views here.

def index(request):
    salesmen = Salesmen.objects.all()
    cont = {
        'salesmen': salesmen
    }
    return render(request, 'salesmen/index.html', cont)

class SalesmenCreateView(CreateView):
    model = Salesmen
    success_url = '/salesmen/'
    template_name = "salesmen/create.html"
    form_class = SalesmenForm

class SalesmenDetailView(DetailView):
    model = Salesmen
    template_name = 'salesmen/detail.html'
    context_object_name = 'salesman'

class SalesmenUpdateView(UpdateView):
    model = Salesmen
    template_name = "salesmen/create.html"
    form_class = SalesmenForm
    
class SalesmenDeleteView(DeleteView):
    model = Salesmen
    success_url = '/salesmen/'
    template_name = "salesmen/delete.html"   