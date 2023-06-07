from django import forms
from .models import Persona,Mascota

class frmPersona(forms.ModelForm):

    class Meta:
        model=Persona
        fields=["rut","nombre","apellido","f_nacimiento","sexo"]

class frmUpdatePersona(forms.ModelForm):

    class Meta:
        model=Persona
        fields=["nombre","apellido","f_nacimiento","sexo"]
        #fields=["nombre","apellido","sexo"]

class frmCrearMascota(forms.ModelForm):

    class Meta:
        model=Mascota
        fields=["id","nombre","tipo","precio"]