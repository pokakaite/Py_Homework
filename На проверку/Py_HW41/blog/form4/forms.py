from .models import Form4
from django.forms import ModelForm, NumberInput

class Form4_Form(ModelForm):
    class Meta:
        model = Form4

        fields = ['year']

        widgets = {
            'year':NumberInput(attrs={
                'min': '1',
                'max': '3000',
            })
        }