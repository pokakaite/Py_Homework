from .models import Form3
from django.forms import ModelForm, TextInput, NumberInput, Textarea, ChoiceField, RadioSelect, CheckboxInput

class Form3_Form(ModelForm):
    class Meta:
        model = Form3
        fields = ['name', 'surname', 'age', 'email', 'gender', 'address', 'agreement']

        widgets = {
            'name':TextInput(attrs={
                'class':'m-2 p-2 border-2 block',
                'placeholder':'Имя'
            }),

            'surname':TextInput(attrs={
                'class':'m-2 p-2 border-2 block',
                'placeholder':'Фамилия'
            }),
            
            'age':NumberInput(attrs={
                'class':'m-2 p-2 border-2 block',
            }),

            'email':TextInput(attrs={
                'class':'m-2 p-2 border-2 block',
            }),

            'gender':RadioSelect(),

            'address':Textarea(attrs={
                'class':'m-2 p-2 border-2 block',
                'placeholder':'Адрес'
            }),

            'agreement':CheckboxInput()
        }   
