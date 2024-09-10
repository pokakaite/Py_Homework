from django.forms import ModelForm, TextInput, NumberInput, RadioSelect, DateInput
from .models import Cart, CartProducts

class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['cart_id', 'salesman_id', 'customer_id', 'completed']

    widgets = {
        'cart_id':NumberInput(),
        'salesman_id':NumberInput(),
        'customer_id':NumberInput(),
        'completed':RadioSelect()
    }

class CartProductsForm(ModelForm):
    class Meta:
        model = CartProducts
        fields = ['products', 'cart', 'count', 'date']

    widgets = {
        'products':NumberInput(),
        'cart':NumberInput(),
        'count':NumberInput(),
        'date':DateInput()
    }