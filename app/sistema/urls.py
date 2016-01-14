from django.conf.urls import url
from .views import index, cursillo, tipocursos, eliminarcurso, actualizarcurso, login, deslogueo, error404

urlpatterns = [

    url(r'^$', login, name="logueo"),
    url(r'^error404$', error404),
    url(r'^deslogueo$', deslogueo, name="logout"),
    url(r'^sistema/$', index, name="inicio"),
    url(r'^addtipo/$', tipocursos),
    url(r'^addcurso/$', cursillo),
    url(r'^eliminarcurso/(?P<pk>\d+)$', eliminarcurso),
    url(r'^addcurso/(?P<pk>\d+)$', actualizarcurso),

]
