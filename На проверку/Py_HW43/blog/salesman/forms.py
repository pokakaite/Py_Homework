from django.forms import ModelForm, TextInput, NumberInput, EmailInput, DateInput
from .models import Salesman

class SalesmanForm(ModelForm):
    class Meta:
        model = Salesman
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
        # 'hiring_date':DateInput(),
        
        # 'position':TextInput(attrs={
        #     'class':'form_input',
        #     'placeholder':"Позиция в фирме",
        # }),
    }