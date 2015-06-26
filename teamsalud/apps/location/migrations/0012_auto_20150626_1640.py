# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0011_auto_20150626_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establecimientos',
            name='clasificacion',
            field=models.IntegerField(default=1, choices=[(1, b'CENTROS DE SALUD O CENTROS MEDICOS'), (0, b'CENTROS DE SALUD CON CAMAS DE INTERNAMIENTO')]),
            preserve_default=True,
        ),
    ]
