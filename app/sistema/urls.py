from django.conf.urls import url
from .views import index, cursillo, tipocursos, eliminarcurso, actualizarcurso

urlpatterns = [
    url(r'^$', index, name="inicio"),
    url(r'^addtipo/$', tipocursos),
    url(r'^addcurso/$', cursillo),
    url(r'^eliminarcurso/(?P<pk>\d+)/$', eliminarcurso),
    url(r'^addcurso/(?P<pk>\d+)/$', actualizarcurso),

]
