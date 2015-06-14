# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_auto_20150614_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrobusquedas',
            name='count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
