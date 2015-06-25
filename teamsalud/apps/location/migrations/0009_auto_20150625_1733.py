# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0008_auto_20150625_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrobusquedas',
            name='count',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
