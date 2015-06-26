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


class Establecimientos(models.Model):
    TIPO_UNO = 1
    TIPO_DOS = 0

    CAT_UNO = 1
    CAT_DOS = 2
    CAT_TRES = 3

    DISTRITO_UNO = 150130
    DISTRITO_DOS = 150114
    DISTRITO_TRES = 150116
    DISTRITO_CUATRO = 150115
    DISTRITO_CINCO = 150134
    DISTRITO_SEIS = 150140
    DISTRITO_SIETE = 150141
    DISTRITO_OCHO = 150122
    DISTRITO_NUEVE = 150131

    INSTITUCION_UNO = 1
    INSTITUCION_DOS = 2
    INSTITUCION_TRES = 3
    INSTITUCION_CUATRO = 4

    CHOICE_CLASIFICACION = (
        (TIPO_UNO, 'CENTROS DE SALUD O CENTROS MEDICOS'),
        (TIPO_DOS, 'CENTROS DE SALUD CON CAMAS DE INTERNAMIENTO')
    )
    CHOICE_CATEGORIA = (
        (CAT_UNO, 'I-3'),
        (CAT_DOS, 'I-4'),
        (CAT_TRES, 'III-1')
    )
    CHOICE_DISTRITO = (
        (DISTRITO_UNO, 'San Borja'),
        (DISTRITO_DOS, 'La Molina'),
        (DISTRITO_TRES, 'Lince'),
        (DISTRITO_CUATRO, 'La Victoria'),
        (DISTRITO_CINCO, 'San Luis'),
        (DISTRITO_SEIS, 'Santiago de Surco'),
        (DISTRITO_SIETE, 'Surquillo'),
        (DISTRITO_OCHO, 'Miraflores'),
        (DISTRITO_NUEVE, 'San Isidro')
    )

    CHOICE_INSTITUCION = (
        (INSTITUCION_UNO, 'MINSA'),
        (INSTITUCION_DOS, 'PUESTOS DE SALUD O POSTAS DE SALUD'),
        (INSTITUCION_TRES, 'PRIVADO'),
        (INSTITUCION_CUATRO, 'GOBIERNO REGIONAL')
    )

    codigo =models.CharField(
        max_length=50
    )
    nombre = models.CharField(
        max_length=200
    )
    clasificacion = models.SmallIntegerField(
        choices=CHOICE_CLASIFICACION,
        default=TIPO_UNO
    )
    ubigeo = models.SmallIntegerField(
        choices=CHOICE_DISTRITO,
        default=DISTRITO_UNO
    )
    direccion = models.CharField(
        max_length=300
    )
    categoria = models.SmallIntegerField(
        choices=CHOICE_CATEGORIA,
        default=CAT_UNO
    )
    tipo_institucion = models.SmallIntegerField(
        choices=CHOICE_INSTITUCION,
        default=INSTITUCION_UNO
    )
    telefono = models.CharField(
        max_length=15
    )
    horario = models.CharField(
        max_length=100
    )
    latitud = models.CharField(
        max_length=50
    )
    longitud = models.CharField(
        max_length=50
    )

    def __unicode__(self):
        return self.nombre


__all__ = [
    'TipoCategoria',
    'Condicion',
    'SignoAlerta',
    'CondicionSignoAlerta',
    'RegistroBusquedas',
    'Servicios',
    'Especialidades',
    'RenaesServicios',
    'Establecimientos'
]
