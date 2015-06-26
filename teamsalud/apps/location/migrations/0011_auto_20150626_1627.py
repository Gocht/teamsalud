# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0010_establecimientos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='establecimientos',
            name='distrito',
        ),
        migrations.AlterField(
            model_name='establecimientos',
            name='ubigeo',
            field=models.SmallIntegerField(default=150130, choices=[(150130, b'San Borja'), (150114, b'La Molina'), (150116, b'Lince'), (150115, b'La Victoria'), (150134, b'San Luis'), (150140, b'Santiago de Surco'), (150141, b'Surquillo'), (150122, b'Miraflores'), (150131, b'San Isidro')]),
            preserve_default=True,
        ),
    ]
