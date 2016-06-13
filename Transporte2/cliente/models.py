from __future__ import unicode_literals

from django.db import models

# Create your models here.

class cliente(models.Model):
    Cedula = models.CharField(max_length=20,null=True)
    Nombre = models.CharField(max_length=20,null=True)
    Apellido = models.CharField(max_length=20,null=True)
    Edad = models.IntegerField(null=True)
    Sexo = models.NullBooleanField()
    Telefono = models.IntegerField(null=True)
    Correo = models.EmailField(null=True)
    Clave = models.CharField(max_length=32,null=True)


    def __str__(self):
        return self.Cedula
