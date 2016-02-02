from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import auth
from .forms import tipocursoForm, cursoForm
from .models import tipocurso, curso
import csv, codecs
# Create your views here.
def dcsv(request):
    if request.POST and request.FILES:
        csvfile = request.FILES['csv_file']
        print(csvfile)
        dialect = csv.Sniffer().sniff(csvfile).read(1024)
        csvfile.open()
        with open(csvfile, newline='') as f:
            reader = csv.reader(f)
            for i,row in enumerate(reader):
                print('Persona: ' + str(i + 1))
                print('------------')
                print(row[0] +  row[1] + row[2]  + row[3]  + row[4]  + row[5]  + row[6] + row[7] + row[8]  + row[9])
                print('\n')
        #dialect = csv.Sniffer().sniff(codecs.encode(csvfile, 'utf-8').read(1024))
        #csvfile.open()
        #reader = csv.reader(codecs.encode(csvfile,'utf-8'), delimiter=',', dialect=dialect)

    return render(request, "csv.html")

def error404(request):
    return render(request, 'error404.html')

def deslogueo(request):
    logout(request)
    return HttpResponseRedirect("/")

def login(request):
    u = request.user
    if u.is_anonymous():
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect("/sistema")

                else:
                    return HttpResponse("Cuenta desactivada")
            else:
                return HttpResponse("datos falsos")
        else:
            return render(request, 'login.html')
    else:
        return HttpResponseRedirect("/sistema")

@login_required(login_url='/error404')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/error404')
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

@login_required(login_url='/error404')
def cursillo(request):
    cu = curso.objects.all()
    formulario = cursoForm()

    if request.method == "POST":
        f = cursoForm(request.POST)
        if f.is_valid():
            f.save()
        else:
            formulario = f

    return render(request, 'curso.html', {'formu': formulario, 'cursos':cu })

@login_required(login_url='/error404')
def actualizarcurso(request, pk):
    a = get_object_or_404(curso, pk= int(pk))
    formulario = cursoForm(instance = a)

    if request.method == "POST":

        f = cursoForm(request.POST, instance = a)

        if f.is_valid():
            f.save()
            return HttpResponseRedirect("/addcurso")
        else:
            formulario = f

    return render(request, 'actualiza_curso.html', {'formu': formulario})

@login_required(login_url='/error404')
def eliminarcurso(request, pk):
    u = curso.objects.get(pk=int(pk)).delete()
    return HttpResponseRedirect("/addcurso")
