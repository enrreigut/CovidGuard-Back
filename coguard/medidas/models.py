from django.db import models


class Niveles(models.Model):

    NIVELES_ENUM = [
        ('0', 'Sin Alerta'),
        ('1', 'Nivel 1'),
        ('2', 'Nivel 2'),
        ('3', 'Nivel 3'),
        ('4', 'Nivel 4'),
        ('5', 'Nivel 4 I'),
        ('6', 'Nivel 4 II'),
    ]

    nivel = models.CharField(max_length=5, choices=NIVELES_ENUM, blank=True, null=True)


class MedidasGenerales(models.Model):
    fecha_creacion = models.DateField(blank=True, null=True)