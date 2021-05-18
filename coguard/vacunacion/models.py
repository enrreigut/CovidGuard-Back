from django.db import models

# Create your models here.
class Vacuna(models.Model):
    nombre = models.CharField(blank=False, null=False, max_length=20)
    apodo = models.CharField(blank=True, null=True, max_length=20)
    dias_hasta_efectividad = models.IntegerField(blank=True, null=True)
    numero_de_dosis = models.IntegerField(blank=True, null=True)
    intervalo_dosis = models.CharField(blank=True, null=True, max_length=50)
    
    def __str__(self):
        return self.nombre