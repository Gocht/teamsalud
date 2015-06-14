# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20150614_0714'),
    ]

    operations = [
        migrations.CreateModel(
            name='RenaesEspecialidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_renaes', models.CharField(max_length=50)),
                ('especialidad', models.ForeignKey(related_name='especialiad_set', to='location.Especialidades')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
