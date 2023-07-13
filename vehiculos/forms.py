from django import forms
from .models import Vehiculo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo 
        fields = ['patente', 'marca', 'modelo', 'categoria', 'imagen']
        labels ={
            'patente':'Patente',
            'marca' : 'Marca',
            'modelo': 'Modelo',
            'categoria':'Categoria',
            'imagen':'Imagen'
        }
        widgets={

            'patente':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese codigo producto...',
                    'id': 'patente',
                    'class': 'form-control',
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese marca producto...',
                    'id':'marca',
                    'class':'form-control',
                }
            ),
            'modelo': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese modelo producto...',
                    'id':'modelo',
                    'class':'form-control',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'id':'categoria',
                    'class':'form-control',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id': 'imagen',
                }
            )
        }