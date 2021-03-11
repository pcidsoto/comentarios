from django import forms
from .models import Comentario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type':'email'}),
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
        }
        #fields = '__all__'
        fields = ['nombre', 'email', 'texto']