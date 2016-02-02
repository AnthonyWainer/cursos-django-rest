from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from .models import curso, tipocurso
from .serializers import CursoSerializer, TipoSerializer


class CursosGroup(viewsets.ModelViewSet):
    queryset = curso.objects.all()
    serializer_class = CursoSerializer

class TipoGroup(viewsets.ModelViewSet):
    queryset = tipocurso.objects.all()
    serializer_class = TipoSerializer
