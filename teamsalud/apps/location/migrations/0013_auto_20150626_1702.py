# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0012_auto_20150626_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='establecimientos',
            name='tipo_institucion',
            field=models.SmallIntegerField(default=1, choices=[(1, b'MINSA'), (2, b'PUESTOS DE SALUD O POSTAS DE SALUD'), (3, b'PRIVADO'), (4, b'GOBIERNO REGIONAL')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='establecimientos',
            name='clasificacion',
            field=models.SmallIntegerField(default=1, choices=[(1, b'CENTROS DE SALUD O CENTROS MEDICOS'), (0, b'CENTROS DE SALUD CON CAMAS DE INTERNAMIENTO')]),
            preserve_default=True,
        ),
    ]
