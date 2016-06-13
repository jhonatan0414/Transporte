from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ruta(models.Model):
    CodigoRuta = models.CharField(max_length=20,null=True)
    IdConductor = models.IntegerField(null=True)
    Codigo_Vehiculo = models.IntegerField(null=True)
    #Horario = models.DateTimeField()
    Lugares = models.IntegerField(null=True)


    def __str__(self):
        return self.CodigoRuta
