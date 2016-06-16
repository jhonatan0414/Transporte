#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import cliente

class clienteForm(forms.ModelForm):
    Cedula = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese cedula del cliente'}))
    Nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese nombre del cliente'}))
    Apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese apellido del cliente'}))
    Edad = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'error','placeholder': 'Ingrese edad del cliente'}))
    Sexo = forms.NullBooleanField(widget = forms.CheckboxInput)
    Telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'error','placeholder': 'Ingrese telefono del cliente'}))
    Correo = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'error','placeholder': 'Ingrese correo del cliente'}))
    Clave = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese contraseña del cliente'}))
    class Meta:
        model = cliente
        fields = ['Cedula','Nombre','Apellido','Edad','Sexo','Telefono','Correo','Clave']
