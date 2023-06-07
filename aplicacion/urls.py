from django.contrib import admin
from django.urls import include, path
from .views import crearmascota, index,informacion,personas,mascotas,crearpersona, updatemascota,updatepersona, \
    eliminarpersona,deletemascota
# URLS.py APLICACION
urlpatterns = [
    path('',index,name='index'),
    path('informacion',informacion,name='informacion'),
    path('personas',personas,name="personas"),
    path('mascotas',mascotas,name="mascotas"),
    path('crearpersona',crearpersona,name="crearpersona"),
    path('updatepersona/<id>',updatepersona,name="updatepersona"),
    path('eliminarpersona/<id>',eliminarpersona,name="eliminarpersona"),
    path('crearmascota',crearmascota,name="crearmascota"),
    path('updatemascota/<id>',updatemascota,name="updatemascota"),
    path('deletemascota/<id>',deletemascota,name="deletemascota")
]