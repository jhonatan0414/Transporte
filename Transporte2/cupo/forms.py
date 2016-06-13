#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import cupo

class clienteForm(forms.ModelForm):
    Codigo = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese un codigo'}))
    CodigoRuta = forms.ModelChoiceField( queryset = ruta.objects.all() )
    Cedula = forms.ModelChoiceField( queryset = cliente.objects.all() )
    Reserva = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'error','placeholder': 'Ingrese la reserva'}))
    class Meta:
        model = cupo
        fields = ['Codigo','CodigoRuta','Cedula','Reserva']
