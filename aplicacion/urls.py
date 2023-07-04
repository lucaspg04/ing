from django.contrib import admin
from django.urls import include, path
from .views import crearmascota, index,personas,mascotas,crearpersona, updatemascota,updatepersona, \
    eliminarpersona,deletemascota,productosuser, registro, productosuser, crear_usuario
# URLS.py APLICACION
urlpatterns = [
    path('',index,name='index'),
    path('productosuser',productosuser,name="productosuser"),
    path('personas',personas,name="personas"),
    path('mascotas',mascotas,name="mascotas"),
    path('crearpersona',crearpersona,name="crearpersona"),
    path('updatepersona/<id>',updatepersona,name="updatepersona"),
    path('eliminarpersona/<id>',eliminarpersona,name="eliminarpersona"),
    path('crearmascota',crearmascota,name="crearmascota"),
    path('updatemascota/<id>',updatemascota,name="updatemascota"),
    path('deletemascota/<id>',deletemascota,name="deletemascota"),
    path("productosuser/", productosuser, name="productosuser"),
    path('registro', registro, name="registro"),
    path('crearempleado', crear_usuario, name="crearempleado")
]