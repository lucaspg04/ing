from django.shortcuts import render,get_object_or_404,redirect
from datetime import date
from .models import Persona,Mascota
from .forms import frmPersona, frmUpdatePersona, frmCrearMascota

# Create your views here.
def index(request):
    return render(request,'aplicacion/index.html')

def mascotas(request):
    pets=Mascota.objects.all()

    contexto={
        "pets":pets
    }

    return render(request,"aplicacion/mascotas/mascotas.html",contexto)

def crearmascota(request):
    form=frmCrearMascota(request.POST or None)

    contexto={
        "form":form
    }

    if request.method=="POST":

        if form.is_valid():
            form.save()
            return redirect(to="mascotas")

    return render(request,"aplicacion/mascotas/crear.html",contexto)

def updatemascota(request,id):
    mascota=get_object_or_404(Mascota,id=id)

    form=frmCrearMascota(instance=mascota)
    contexto={
        "form":form,
        "mascota":mascota
    }

    if request.method=="POST":

        form=frmCrearMascota(data=request.POST,instance=mascota)

        if form.is_valid():
            
            datos=form.cleaned_data
            pet=Mascota.objects.get(id=mascota.id)
            #pet.id=datos.get("id")
            pet.tipo=datos.get("tipo")
            pet.nombre=datos.get("nombre")

            pet.save()
            return redirect(to="mascotas")

    return render(request,"aplicacion/mascotas/update.html",contexto)

def deletemascota(request,id):
    mascota=get_object_or_404(Mascota,id=id)


    contexto={
 
        "pet":mascota
    }

    if request.method=="POST":
        mascota.delete()
        return redirect(to="mascotas")


    return render(request,"aplicacion/mascotas/delete.html",contexto)

def personas(request):
    people=Persona.objects.all()
    
    contexto={
        "personas":people
    }
    

 
    return render(request,"aplicacion/personas/personas.html",contexto)

def crearpersona(request):
    form=frmPersona(request.POST or None)

    contexto={
        "form":form
    }

    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(to="personas")
        

    return render(request,"aplicacion/personas/crearpersona.html",contexto)


def updatepersona(request,id):
    persona=get_object_or_404(Persona,rut=id)

    form=frmUpdatePersona(instance=persona)
    contexto={
        "form":form,
        "persona":persona
    }

    if request.method=="POST":

        form=frmUpdatePersona(data=request.POST,instance=persona)

        if form.is_valid():
            
            datos=form.cleaned_data
            mpersona=Persona.objects.get(rut=persona.rut)
            mpersona.nombre=datos.get("nombre")
            mpersona.apellido=datos.get("apellido")
            mpersona.f_nacimiento=datos.get("f_nacimiento")
            mpersona.sexo=datos.get("sexo")
            mpersona.save()
            return redirect(to="personas")

    return render(request,"aplicacion/personas/update.html",contexto)

def eliminarpersona(request,id):
    persona=get_object_or_404(Persona,rut=id)

    try:
        pet=Mascota.objects.get(persona=persona)
    
    except:
        pet=None

    #print("**********************",pet)

    contexto={
 
        "persona":persona,
        "pet":pet
    }

    if request.method=="POST":
        persona.delete()
        return redirect(to="personas")


    return render(request,"aplicacion/personas/delete.html",contexto)

#pagina que no sirve para nada
def informacion(request):
    fecha=date.today()
    autor="El profe"
    animales=["perro","gato","ñu","narval","manati","womba"]
    people=Persona.objects.all()
   

    contexto={
        "hoy":fecha,
        "autor":autor,
        "animales":animales,
        "people":people
    }

    return render(request,'aplicacion/informacion.html',contexto)