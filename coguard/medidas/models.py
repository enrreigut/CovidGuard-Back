from django.db import models

class Medidas(models.Model):

    municipio = models.CharField(blank=True, null=True, max_length=150)

    fecha_creacion = models.DateField(blank=True, null=True)

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

    cierre_perimetral = models.BooleanField(blank=True, null=True)

    horarios_ocio_nocturno = models.CharField(blank=True, null=True, max_length=5)

    aforo_ocio_nocturno_exterior = models.CharField(blank=True, null=True, max_length=5)

    aforo_ocio_nocturno_interior = models.CharField(blank=True, null=True, max_length=5)

    horario_hosteleria = models.CharField(blank=True, null=True, max_length=5)

    aforo_hosteleria_nocturno_exterior = models.CharField(blank=True, null=True, max_length=5)

    aforo_hosteleria_nocturno_interior = models.CharField(blank=True, null=True, max_length=5)

    def __str__(self):
        return self.municipio + "(" + str(self.fecha_creacion) + ")"