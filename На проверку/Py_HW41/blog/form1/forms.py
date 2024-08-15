from .models import Form1
from django.forms import ModelForm, TextInput

class Form1_Form(ModelForm):
    class Meta:
        model = Form1
        fields = ['login', 'password']

        widgets = {
            'login':TextInput(attrs={
                'class':'login'
            }),
            'password':TextInput(attrs={
                'class':'password'
            })
        }

