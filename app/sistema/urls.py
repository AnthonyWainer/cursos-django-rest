from django.conf.urls import url
from .views import index, curso, tipocursos

urlpatterns = [
    url(r'^$', index, name="inicio"),
    url(r'^addtipo/$', tipocursos),
    url(r'^addcurso/$', curso),
]
