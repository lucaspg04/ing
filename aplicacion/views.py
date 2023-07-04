from django.shortcuts import render,get_object_or_404,render, redirect
from datetime import date
from .models import Persona,Mascota, Producto
from .forms import frmPersona, frmUpdatePersona, frmCrearMascota,  frmRegistro
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


# Create your views here.
def index(request):
    return render(request,'aplicacion/index.html')

def productosuser(request):
    return render(request,'aplicacion/productouser.html')

def listarproducto(request):
    productos=Producto.objects.all()
    
    contexto={
        "products":productos
    }
    return render(request,'aplicacion/index.html', contexto)

def productosuser(request):
    return render(request,'aplicacion/productouser.html')

def registro(request):

    contexto={
        "form": frmRegistro
    }
    
    if request.method == 'POST':
        formulario = frmRegistro(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Te has registrado correctamente!")
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")
        else:
            for msg in formulario.error_messages:
                messages.error(request, formulario.error_messages[msg])
    return render(request, 'registration/registro.html', contexto) 

@login_required
def mascotas(request):
    pets=Mascota.objects.all()

    contexto={
        "pets":pets
    }

    return render(request,"aplicacion/mascotas/mascotas.html",contexto)

@login_required
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

@login_required
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
            pet.tipo=datos.get("tipo")
            pet.nombre=datos.get("nombre")

            pet.save()
            return redirect(to="mascotas")

    return render(request,"aplicacion/mascotas/update.html",contexto)

@login_required
def deletemascota(request,id):
    mascota=get_object_or_404(Mascota,id=id)


    contexto={

        "pet":mascota
    }

    if request.method=="POST":
        mascota.delete()
        return redirect(to="mascotas")


    return render(request,"aplicacion/mascotas/delete.html",contexto)

@login_required
def personas(request):
    people=Persona.objects.all()
    
    contexto={
        "personas":people
    }
    
    return render(request,"aplicacion/personas/personas.html",contexto)

@login_required
def crearpersona(request):
    formulario = frmPersona(request.POST or None)

    if request.method == "POST":
        if formulario.is_valid():
            persona = formulario.save(commit=False)
            # Realizar las validaciones necesarias antes de guardar los cambios
            persona.save()
            return redirect(to="personas")
        else:
            messages.error(request, "Error: Completa todos los campos y/o verifica el Rut")

    contexto = {
        "form": formulario
    }

    return render(request, "aplicacion/personas/crearpersona.html", contexto)




@login_required
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

@login_required
def eliminarpersona(request,id):
    persona=get_object_or_404(Persona,rut=id)

    try:
        pet=Mascota.objects.get(persona=persona)
    
    except:
        pet=None

    contexto={

        "persona":persona,
        "pet":pet
    }

    if request.method=="POST":
        persona.delete()
        return redirect(to="personas")


    return render(request,"aplicacion/personas/delete.html",contexto)


@login_required
def crear_usuario(request):
    grupos = Group.objects.all()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo_id = request.POST.get('grupo')
            grupo = Group.objects.get(id=grupo_id)
            user.groups.add(grupo)
            return redirect('index')
    else:
        form = UserCreationForm()
    
    context = {'form': form, 'grupos': grupos}
    return render(request, 'aplicacion/crearempleado.html', context)
