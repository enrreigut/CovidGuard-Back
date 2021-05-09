from django.db import models


class EstadisticasTipo1(models.Model):
    fecha_creacion = models.DateField(blank=True, null=True)
    lugar_de_residencia = models.CharField(blank=True, null=True, max_length=150)
    total_confirmados = models.IntegerField(blank=True, null=True)
    tasa_total_confirmados = models.FloatField(blank=True, null=True)
    confirmados_PDIA = models.IntegerField(blank=True, null=True)
    tasa_PDIA = models.FloatField(blank=True, null=True)
    confirmados_PDIA_14 = models.IntegerField(blank=True, null=True)
    tasa_PDIA_14 = models.FloatField(blank=True, null=True)
    confirmados_PDIA_7 = models.IntegerField(blank=True, null=True)
    tasa_PDIA_7 = models.FloatField(blank=True, null=True)
    curados = models.IntegerField(blank=True, null=True)
    fallecidos = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.lugar_de_residencia + "(" + str(self.total_confirmados) +")"
