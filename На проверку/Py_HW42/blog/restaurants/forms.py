from .models import Restaurants
from django.forms import ModelForm, TextInput, NumberInput

class Restaurants_Form(ModelForm):
    class Meta:
        model = Restaurants
        fields = ['name', 'cuisine', 'address', 'web_site', 'contacts']

        widgets = {
            'name':TextInput(),
            'cuisine':TextInput(),
            'address':TextInput(),
            'web_site':TextInput(),
            'contacts':NumberInput()
        }