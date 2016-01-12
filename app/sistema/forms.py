from django import forms

class tipocursoForm(forms.Form):
    descripciontipocurso = forms.CharField(label='Descripción tipo curso', max_length=15, widget=forms.TextInput(attrs={'class':'form-control'}))