from django import forms
from .models import curso

class tipocursoForm(forms.Form):
    at = {'class':'form-control', 'placeholder':'ingresar tipo de curso'}
    descripciontipocurso = forms.CharField(label='Descripción tipo curso', max_length=15, widget=forms.TextInput(attrs=at))

class cursoForm(forms.ModelForm):
    class Meta:
        dc = {'class':'form-control', 'placeholder':'ingresar descripción de curso'}
        tp = {'class':'form-control'}
        c = ciclos = (
                ('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV','IV'),
                ('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII','VIII'),
                ('IX', 'IX'), ('X', 'X'), ('E', 'E'),
            )
        model = curso
        exclude = {'estadocurso'}
        fields = '__all__'
        labels = {
            'descripcioncurso' : ('Descripcion del curso'),
            'tipocurso'        : ('Tipo curso'),
        }
        widgets = {
            'descripcioncurso' : forms.TextInput(attrs=dc),
            'tipocurso'        : forms.Select(attrs=tp),
            'creditos'         : forms.NumberInput(attrs=tp),
            'ciclo'            : forms.Select(attrs=tp, choices=c)
        }
        help_texts = {
            'creditos': ('** No escribir mas de 5 créditos.<br>'),
        }
        error_messages = {
            'creditos': {
                'max_length': ("Crédito Muy largo."),
            },
        }
