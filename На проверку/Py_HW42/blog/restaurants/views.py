from django.shortcuts import render
from .forms import Restaurants_Form
from .models import Restaurants
from django.views.generic import CreateView, DeleteView, DetailView

# Create your views here.

def index(request):
    restaurants = Restaurants.objects.order_by()[::]
    cont = {
        'restaurants': restaurants
    }
    return render(request, 'index.html', cont)

class CreateRestaurant(CreateView):
    model = Restaurants
    success_url = '/show/'
    template_name = "create.html"
    form_class = Restaurants_Form

class ShowRestaurants(DetailView):
    model = Restaurants
    success_url = '/show/'
    template_name = "show.html"
    context_object_name = 'restaurant'
    form_class = Restaurants_Form

class DeleteRestaurant(DeleteView):
    model = Restaurants
    success_url = '/restaurants/'
    template_name = "delete.html"
    form_class = Restaurants_Form

class EditRestaurant(DeleteView):
    model = Restaurants
    success_url = '/restaurants/'
    template_name = "create.html"
    form_class = Restaurants_Form

class SearchRestaurant(DetailView):
    model = Restaurants
    success_url = '/restaurants/'
    template_name = "show.html"
    form_class = Restaurants_Form

