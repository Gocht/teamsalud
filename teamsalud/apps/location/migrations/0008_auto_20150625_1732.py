# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0007_renaesespecialidades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrobusquedas',
            name='count',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
