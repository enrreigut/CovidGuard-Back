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

    def parse(self):
        res = "<b>Estadísticas del:</b> " + str(self.fecha_creacion) + "\n\n"

        res += "<b>Total Confirmados:</b> " + str(self.total_confirmados) + "\n"
        res += "<b>Tasa Total Confirmados:</b> " + str(round(self.tasa_total_confirmados, 2)) + "\n\n"
        res += "<b>Confirmados PDIA:</b> " + str(self.confirmados_PDIA) + "\n"
        res += "<b>Tasa PDIA:</b> " + str(round(self.tasa_PDIA, 2)) + "\n\n"
        res += "<b>Confirmados PDIA 14:</b> " + str(self.confirmados_PDIA_14) + "\n"
        res += "<b>Tasa PDIA 14:</b> " + str(round(self.tasa_PDIA_14, 2)) + "\n\n"
        res += "<b>Confirmados PDIA 7:</b> " + str(self.confirmados_PDIA_7) + "\n"
        res += "<b>Tasa PDIA 7:</b> " + str(round(self.tasa_PDIA_7, 2)) + "\n\n"
        res += "<b>Curados:</b> " + str(self.curados) + "\n"
        res += "<b>Fallecidos:</b> " + str(self.fallecidos) + "\n\n"
        res += "<b><i>PDIA</i></b>: <i>PDIA</i> (Pruebas Diagnósticas de Infección Activa) incluye todos los casos de COVID-19 con infección activa, confirmados por técnica PCR o test antigénicos rápidos de última generación, siguiendo la nueva estrategia de vigilancia del Ministerio de Sanidad. \n"

        return res

    def __str__(self):
        return self.lugar_de_residencia + "(" + str(self.total_confirmados) +")"
