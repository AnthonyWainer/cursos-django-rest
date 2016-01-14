from django.conf.urls import url
from .views import index, cursillo, tipocursos, eliminarcurso, actualizarcurso, deslogueo, error404, login
#from django.contrib.auth.views import login

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
