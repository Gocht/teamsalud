# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CondicionSignoAlerta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extra', models.CharField(max_length=100)),
                ('condicion', models.ForeignKey(related_name='condicion_set', to='location.Condicion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SignoAlerta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoCategoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='condicionsignoalerta',
            name='signo_alerta',
            field=models.ForeignKey(related_name='signo_alerta_set', to='location.SignoAlerta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='condicionsignoalerta',
            name='tipo_categoria',
            field=models.ForeignKey(related_name='tipo_categoria_set', to='location.TipoCategoria'),
            preserve_default=True,
        ),
    ]
