from django.contrib import admin
from .models import Persona, Mascota, Carrito, Producto

# Register your models here.
class admPersona(admin.ModelAdmin):
    list_display=["rut","nombre","apellido","f_nacimiento","sexo"]
    list_editable=["nombre","apellido","f_nacimiento","sexo"]

    class meta:
        model=Persona

class admMascota(admin.ModelAdmin):
    list_display=["id","nombre","tipo",]
    list_editable=["nombre","tipo"]

    class meta:
        model=Mascota

class admCarrito(admin.ModelAdmin):
    list_display=["id","usr","producto","cantidad"]
    
    class meta:
        model=Carrito


class admProducto(admin.ModelAdmin):
    list_display=["id_prod","nombre", "precio"]
    list_editable=["nombre", "precio"]

    class meta:
        model=Producto


admin.site.register(Persona,admPersona)
admin.site.register(Mascota,admMascota)
admin.site.register(Carrito,admCarrito)
admin.site.register(Producto,admProducto)
