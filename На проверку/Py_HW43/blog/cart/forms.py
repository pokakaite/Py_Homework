from .models import Cart
from django.forms import ModelForm, NumberInput, CheckboxInput

class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['order', 'customer_id', 'salesman_id']

    widgets = {
        'order':NumberInput(),
        'customer_id':NumberInput(),
        'salesman_id':NumberInput(),
    }