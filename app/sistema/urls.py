from django.conf.urls import url, include
from rest_framework import routers
from .views import index, cursillo, tipocursos, eliminarcurso, actualizarcurso, deslogueo, error404, login, dcsv
from .viewsets import CursosGroup, TipoGroup
#from django.contrib.auth.views import login

router = routers.DefaultRouter()
router.register(r'cursos', CursosGroup)
router.register(r'tipocurso', TipoGroup)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', login, name="logueo"),
    url(r'^error404$', error404),
    url(r'^csv$', dcsv, name="csv"),
    url(r'^deslogueo$', deslogueo, name="logout"),
    url(r'^sistema/$', index, name="inicio"),
    url(r'^addtipo/$', tipocursos),
    url(r'^addcurso/$', cursillo),
    url(r'^eliminarcurso/(?P<pk>\d+)$', eliminarcurso),
    url(r'^addcurso/(?P<pk>\d+)$', actualizarcurso),

]
