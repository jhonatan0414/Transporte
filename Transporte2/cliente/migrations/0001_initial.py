# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cedula', models.IntegerField(null=True)),
                ('Nombre', models.CharField(max_length=20, null=True)),
                ('Apellido', models.CharField(max_length=20, null=True)),
                ('Edad', models.IntegerField(null=True)),
                ('Sexo', models.NullBooleanField()),
                ('Telefono', models.IntegerField(null=True)),
                ('Correo', models.EmailField(max_length=254, null=True)),
                ('Clave', models.CharField(max_length=32, null=True)),
            ],
        ),
    ]