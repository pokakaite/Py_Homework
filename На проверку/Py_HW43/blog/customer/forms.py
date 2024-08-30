from django.forms import ModelForm, TextInput, NumberInput, EmailInput
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'last_name', 'number', 'email']

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
        }),
    }