# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0009_auto_20150625_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Establecimientos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=200)),
                ('clasificacion', models.SmallIntegerField(default=1, choices=[(1, b'CENTROS DE SALUD O CENTROS MEDICOS'), (0, b'CENTROS DE SALUD CON CAMAS DE INTERNAMIENTO')])),
                ('distrito', models.SmallIntegerField(default=1, choices=[(1, b'San Borja'), (2, b'La Molina'), (3, b'Lince'), (4, b'La Victoria'), (5, b'San Luis')])),
                ('ubigeo', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=300)),
                ('categoria', models.SmallIntegerField(default=1, choices=[(1, b'I-3'), (2, b'I-4'), (3, b'III-1')])),
                ('telefono', models.CharField(max_length=15)),
                ('horario', models.CharField(max_length=100)),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
