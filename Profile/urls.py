from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from Profile import views

urlpatterns = [
    re_path(r'Profile_Lista/$', views.ExampleList2.as_view()),
    re_path(r'Ciudad_Lista/$', views.CiudadList2.as_view()),
    re_path(r'Ocupacion_Lista/$', views.OcupacionList2.as_view()),
    re_path(r'Estado_Lista/$', views.EstadoList2.as_view()),
    re_path(r'EstadoCivil_Lista/$', views.EstadoCivilList2.as_view()),
    re_path(r'Genero_Lista/$', views.GeneroList2.as_view())
]
