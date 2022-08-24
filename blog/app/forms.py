from django import forms
from django.forms import ModelForm

from .models import Publicacion

class PublicacionForm(ModelForm):
    class Meta:
        model = Publicacion
        fields = ('titulo', 'descripcion', 'email')
        labels = {
            'titulo':'Titulo',
            'descripcion': 'Descripcion',
            'email':'Email',
        }
        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }