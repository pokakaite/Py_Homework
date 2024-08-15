from .models import Form2
from django.forms import ModelForm, NumberInput, RadioSelect

class Form2_Form(ModelForm):
    class Meta:
        model = Form2
        fields = ['number_1', 'number_2', 'number_3', 'choice']

        widgets = {
            'number_1':NumberInput(attrs={
                'id':"input1", 
                'class':"number"
            }),
            'number_2':NumberInput(attrs={
                'id':"input2", 
                'class':"number"
            }),
            'number_3':NumberInput(attrs={
                'id':"input3", 
                'class':"number"
            }),
            'choice':RadioSelect(attrs={
                'class':"radio"
            })
        }