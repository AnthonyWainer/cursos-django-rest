from django.conf.urls import url
from .views import index, sumando, dividir

urlpatterns = [
    url(r'^$', index),
    url(r'^suma$', sumando),
    url(r'^div$', dividir),
]