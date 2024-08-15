from .models import Form3
from django.forms import ModelForm, TextInput, NumberInput, Textarea, RadioSelect, CheckboxInput

class Form3_Form(ModelForm):
    class Meta:
        model = Form3
        fields = ['name', 'surname', 'age', 'email', 'gender', 'address', 'agreement']

        widgets = {
            'name':TextInput(attrs={
                'class':'m-2 p-2 border-2 block',
                'placeholder':'Имя',
                'id':'name'
            }),

            'surname':TextInput(attrs={
                'class':'m-2 p-2 border-2 block',
                'placeholder':'Фамилия',
                'id':'surname'

            }),
            
            'age':NumberInput(attrs={
                'class':'m-2 p-2 border-2 block',
                'min': '1',
                'max':'100',
                'id':'age'
            }),

            'email':TextInput(attrs={
                'class':'m-2 p-2 border-2 block',
                'id':'email'
            }),

            'gender':RadioSelect(attrs={
                'checked':'false',
                'id':'gender'
            }),

            'address':Textarea(attrs={
                'class':'m-2 p-2 border-2 block',
                'placeholder':'Адрес',
                'rows': '5',
                'id':'address'
            }),

            'agreement':CheckboxInput(attrs={
                'id':'agreement'
            })
        }   
