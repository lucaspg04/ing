from django import forms
from .models import Persona,Mascota
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class frmPersona(forms.ModelForm):

    class Meta:
        model=Persona
        fields=["rut","nombre","apellido","f_nacimiento","sexo"]

class frmUpdatePersona(forms.ModelForm):

    class Meta:
        model=Persona
        fields=["nombre","apellido","f_nacimiento","sexo"]

class frmCrearMascota(forms.ModelForm):

    class Meta:
        model=Mascota
        fields=["nombre","tipo","desc","precio"]
        
        
class frmRegistro(UserCreationForm):
    
    class Meta:
        model=User
        fields=["username","email","password1","password2",]
            
