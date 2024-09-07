from django.forms import ModelForm, TextInput, NumberInput, Textarea
from .models import Products

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['product_id', 'name', 'description', 'price']

    widgets = {
        'name':TextInput(attrs={
            'class':'form_input',
            'placeholder':"Название",
        }),
        'description':Textarea(attrs={
            'class':'form_input',
            'placeholder':"Описание",
        }),
        'price':NumberInput(attrs={
            'class':'form_input',
            'placeholder':"Цена",
        }),
    }