from django.db import models

# Create your models here.

class TipoCategoria(models.Model):
    codigo = models.CharField(
        max_length=10
    )
    def __unicode__(self):
        return self.codigo


class Condicion(models.Model):
    codigo = models.CharField(
        max_length=50
    )
    nombre = models.CharField(
        max_length=300
    )
    def __unicode__(self):
        return self.codigo


class SignoAlerta(models.Model):
    codigo = models.CharField(
        max_length=50
    )
    descripcion = models.CharField(
        max_length=300
    )

    def __unicode__(self):
        return self.descripcion


class CondicionSignoAlerta(models.Model):

    condicion = models.ForeignKey(
        'Condicion',
        related_name='condicion_set',
        )
    signo_alerta = models.ForeignKey(
        'SignoAlerta',
        related_name='signo_alerta_set'
    )
    tipo_categoria = models.ForeignKey(
        'TipoCategoria',
        related_name='tipo_categoria_set'
    )


class RegistroBusquedas(models.Model):

    busqueda = models.ForeignKey(
        'CondicionSignoAlerta',
        related_name='condicion_signo_alerta_set'
    )
    distrito = models.CharField(
        max_length=50
    )
    count = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        unique_together = [("busqueda", "distrito")]


class Servicios(models.Model):
    codigo = models.CharField(
        max_length=50
    )
    descripcion = models.CharField(
        max_length=300
    )
    def __unicode__(self):
        return self.descripcion


class Especialidades(models.Model):
    codigo = models.CharField(
        max_length=50
    )
    descripcion = models.CharField(
        max_length=300
    )
    def __unicode__(self):
        return self.descripcion

class RenaesServicios(models.Model):

    codigo_renaes = models.CharField(
        max_length=50
    )
    servicio = models.ForeignKey(
        'Servicios',
        related_name='servicio_set'
    )

class RenaesEspecialidades(models.Model):
    codigo_renaes = models.CharField(
        max_length=50
    )
    especialidad = models.ForeignKey(
        'Especialidades',
        related_name='especialiad_set'
    )


__all__ = [
    'TipoCategoria',
    'Condicion',
    'SignoAlerta',
    'CondicionSignoAlerta',
    'RegistroBusquedas',
    'Servicios',
    'Especialidades',
    'RenaesServicios'
]
