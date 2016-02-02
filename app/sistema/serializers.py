from rest_framework import serializers
from .models import curso, tipocursofrom 

class TipoSerializer(serializers.HyperlinkedModelSerializer):
    #pcursos = serializers.RelatedField(many  = True)
    class Meta:
        model = tipocurso




class CursoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = curso
        fields = ('id','descripcioncurso','creditos','tipocurso', 'ciclo')
        #depth = 1 #para mostrar todos los datos de la llave foranea


'''class CursoSerializer(serializers.HyperlinkedModelSerializer):
    idplan =  PlanSerializer(read_only=True)
    #idplan =  serializers.PrimaryKeyRelatedField(read_only=True)
    #idplan =  serializers.SlugRelatedField(read_only=True,slug_field='estadoplan')

    class Meta:
        model = cursos
        fields = ('id','descripcioncurso','creditos','tipocurso', 'ciclo', 'idplan')'''
