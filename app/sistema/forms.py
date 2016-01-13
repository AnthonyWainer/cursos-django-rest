from django import forms
from .models import curso

class tipocursoForm(forms.Form):
    at = {'class':'form-control', 'placeholder':'ingresar tipo de curso'}
    descripciontipocurso = forms.CharField(label='Descripción tipo curso', max_length=15, widget=forms.TextInput(attrs=at))

class cursoForm(forms.ModelForm):
    class Meta:
        model = curso
        fields = '__all__'
        dc = {'class':'form-control', 'placeholder':'ingresar descripción de curso'}
        tp = {'class':'form-control'}
        cr = {'class':'form-control', 'placeholder': 'ingrese número de créditos'}
        c = ciclos = (
                ('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV','IV'),
                ('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII','VIII'),
                ('IX', 'IX'), ('X', 'X'), ('E', 'E'),
            )

        exclude = {'estadocurso'}

        labels = {
            'descripcioncurso' : ('Descripcion del curso'),
            'tipocurso'        : ('Tipo curso'),
            'creditos'         : ('Créditos'),
        }
        widgets = {
            'descripcioncurso' : forms.TextInput(attrs=dc),
            'tipocurso'        : forms.Select(attrs=tp),
            'creditos'         : forms.NumberInput(attrs=cr),
            'ciclo'            : forms.Select(attrs=tp, choices=c)
        }
        help_texts = {
            'creditos': ('** No escribir mas de 5 créditos.<br>'),
            'ciclo'   : ('** Seleccione un ciclo.<br>'),
        }
        error_messages = {
            'creditos': {
                'max_length': ("Crédito Muy largo."),
            },
        }
