from __future__ import unicode_literals

from django.db import models
from ruta.models import ruta
from cliente.models import cliente
# Create your models here.

class cupo(models.Model):
    Codigo = models.CharField(max_length=20,primary_key=True)
    CodigoRuta = models.ForeignKey(ruta, null=True)
    Cedula = models.ForeignKey(cliente, null=True)
    Reserva = models.IntegerField()


    def __str__(self):
        return self.Codigo
