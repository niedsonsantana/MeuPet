from django import forms
from .models import Animal



class AnimalModelForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields=['nome', 'porte', 'cor', 'castrado', 'tipo', 'image', 'info']
