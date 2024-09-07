from django.forms import ModelForm, TextInput, NumberInput, EmailInput
from .models import Customers

class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['customer_id', 'name', 'last_name', 'number', 'email']

    widgets = {
        'name':TextInput(attrs={
            'class':'form_input',
            'placeholder':"Имя",
        }),
        'last_name':TextInput(attrs={
            'class':'form_input',
            'placeholder':"Фамилия",
        }),
        'number':NumberInput(attrs={
            'class':'form_input',
            'placeholder':"Номер телефона",
        }),
        'e-mail':EmailInput(attrs={
            'class':'form_input',
            'placeholder':"E-mail",
        })
    }