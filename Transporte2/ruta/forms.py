#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import ruta

class clienteForm(forms.ModelForm):
    CodigoRuta = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese una ruta'}))
    IdConductor = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'error','placeholder': 'Ingrese id. del conductor '}))
    Codigo_Vehiculo = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'error','placeholder': 'Ingrese id. del vehiculo'}))
    Lugares = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'error','placeholder': 'Ingrese lugares'}))
    class Meta:
        model = ruta
        fields = ['CodigoRuta','IdConductor','Codigo_Vehiculo','Lugares']
