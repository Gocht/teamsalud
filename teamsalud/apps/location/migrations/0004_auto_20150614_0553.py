# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_registrobusquedas'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registrobusquedas',
            unique_together=set([('busqueda', 'distrito')]),
        ),
    ]
