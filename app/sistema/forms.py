from django import forms
from .models import curso

class tipocursoForm(forms.Form):
    at = {'class':'form-control', 'placeholder':'ingresar tipo de curso'}
    descripciontipocurso = forms.CharField(label='Descripción tipo curso', max_length=15, widget=forms.TextInput(attrs=at))

class cursoForm(forms.ModelForm):
    class Meta:
        model = curso
        fields = '__all__'
