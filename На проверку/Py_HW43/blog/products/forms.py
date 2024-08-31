from django.forms import ModelForm, TextInput, NumberInput, EmailInput
from .models import Products

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'salesman_id']

    widgets = {
        'name':TextInput(attrs={
            'class':'form_input',
            'placeholder':"Название",
        }),
        'description':TextInput(attrs={
            'class':'form_input',
            'placeholder':"Описание",
        }),
        'price':NumberInput(attrs={
            'class':'form_input',
            'placeholder':"Цена",
        }),
        'salesman_id':NumberInput()
    }