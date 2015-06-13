from django.db import models

# Create your models here.


class TipoCategoria(models.Model):
    codigo=models.CharField(
        max_length=10
    )

    class Meta:
        app_label = 'loc'


class Condicion(models.Model):
    codigo=models.CharField(
        max_length=50
    )
    nombre=models.CharField(
        max_length=300
    )

    class Meta:
        app_label = 'loc'


class SignoAlerta(models.Model):
    codigo=models.CharField(
        max_length=50
    )
    descripcion=models.CharField(
        max_length=300
    )

    class Meta:
        app_label = 'loc'


class CondicionSignoAlerta(models.Model):

    condicion = models.ForeignKey(
        'Condicion',
        related_name='condicion_set',
        )
    signo_alerta=models.ForeignKey(
        'SignoAlerta',
        related_name='signo_alerta_set'
    )
    tipo_categoria=models.ForeignKey(
        'TipoCategoria',
        related_name='tipo_categoria_set'
    )

    class Meta:
        app_label = 'loc'


