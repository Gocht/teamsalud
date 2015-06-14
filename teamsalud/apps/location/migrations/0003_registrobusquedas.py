# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_remove_condicionsignoalerta_extra'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroBusquedas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distrito', models.CharField(max_length=50)),
                ('busqueda', models.ForeignKey(related_name='condicion_signo_alerta_set', to='location.CondicionSignoAlerta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
