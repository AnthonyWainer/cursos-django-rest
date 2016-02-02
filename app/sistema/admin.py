from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class cursoResource(resources.ModelResource):
    class Meta:
        model = curso
# Register your models herecurso
class cursoAdmin(ImportExportModelAdmin):
    resource_class = cursoResource
    pass
admin.site.register(tipocurso)
admin.site.register(curso)
