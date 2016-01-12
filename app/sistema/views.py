from django.shortcuts import render, HttpResponse
from .forms import tipocursoForm, cursoForm
from .models import tipocurso, curso
# Create your views here.
def index(request):
    return render(request, 'index.html')

def tipocursos(request):
    if request.method == "POST": #esto sirve para preguntar si el método es post
        f = tipocursoForm(request.POST) #esto sirve para rescatar los datos del formulario

        if f.is_valid(): #esto sirve para validad formulario
            tp = tipocurso()
            tp.descripciontipocurso = request.POST["descripciontipocurso"]
            tp.save()

            tc = tipocurso.objects.all()
            formulario = tipocursoForm()

        else:
            formulario = f
    else:
        tc = tipocurso.objects.all()
        formulario = tipocursoForm()
    return render(request, 'tipocurso.html', {'formu': formulario, 'tipocurso':tc})

def curso(request):
    formulario = cursoForm()
    return render(request, 'curso.html', {'formu': formulario })
