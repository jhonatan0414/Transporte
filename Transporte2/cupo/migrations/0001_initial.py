# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ruta', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cupo',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Reserva', models.IntegerField()),
                ('Cedula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('CodigoRuta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ruta.ruta')),
            ],
        ),
    ]
