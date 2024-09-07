from django.forms import ModelForm, TextInput, NumberInput, EmailInput, DateInput, RadioSelect
from .models import Salesmen

class SalesmenForm(ModelForm):
    class Meta:
        model = Salesmen
        fields = ['salesman_id', 'name', 'last_name', 'number', 'email', 'date', 'position']

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
        'date':DateInput(),
        
        'position':RadioSelect(attrs={
            'class':'form_input',
            'placeholder':"Позиция в фирме",
        }),
    }