from rest_framework.views import APIView
from django.http import JsonResponse
from estadisticas.utils import *
from vacunacion.utils import *
import json


acciones = {
    'AYUDAS': 'getAyudas',
    'ESTADISTICAS FECHAS': 'getEstadisticasFechas',
    'ESTADISTICAS TIPOS': 'getTiposEstadisticas',
    'ESTADISTICAS GENERALES': 'getEstadisticasGenerales',
    'ESTADISTICAS ESPECIFICAS': 'getEstadisticasEspecificas',
    'EFECTIVIDAD VACUNA': 'getEfectividadVacuna',
    'NUMERO DOSIS VACUNA': 'getNumeroDosisVacuna',
    'INTERVALO DOSIS VACUNA': 'getIntervaloDosisVacuna',
    'INFO GENERAL VACUNA': 'getInfoGeneralVacuna',
    'LISTADO VACUNAS': 'getListadoVacunas',
    'VACUNA POR EDAD': 'getVacunaPorEdad',
}


class WebhookEstadisticasTipo1API(APIView):
    def post(self, request):

        res = {'fulfillmentText': "No te entendí"}

        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
        except Exception as e:
            return JsonResponse({'fulfillmentText': "Error al parsear el cuerpo de la petición (" + e + ")"}, safe=False)

        try:
            action = body['queryResult']['action']
        except Exception as e:
            return JsonResponse({'fulfillmentText': "Error al obtener la acción (" + e + ")"}, safe=False)

        # Estadisticas

        if action == acciones['AYUDAS']:
            res = prettyPrint(getAyudas())
        elif action == acciones['ESTADISTICAS FECHAS']:
            res = prettyPrint(getFechasEstadisticas())
        elif action == acciones['ESTADISTICAS TIPOS']:
            res = prettyPrint(getTipoEstadisticas())
        elif action == acciones['ESTADISTICAS GENERALES']:
            res = prettyPrint(getEstadisticasGenerales(body))
        elif action == acciones['ESTADISTICAS ESPECIFICAS']:
            res = prettyPrint(getEstadisticasEspecificas(body))
        
        # Vacunas
            
        elif action == acciones['EFECTIVIDAD VACUNA']:
            res = prettyPrint(getEfectividadVacuna(body))
        elif action == acciones['NUMERO DOSIS VACUNA']:
            res = prettyPrint(getNumeroDosisVacuna(body))
        elif action == acciones['INTERVALO DOSIS VACUNA']:
            res = prettyPrint(getIntervaloDosisVacuna(body))
        elif action == acciones['INFO GENERAL VACUNA']:
            res = prettyPrint(getInfoGeneralVacuna(body))
        elif action == acciones['VACUNA POR EDAD']:
            res = prettyPrint(getVacunaPorEdad(body))    
        elif action == acciones['LISTADO VACUNAS']:
            res = prettyPrint(getListadoVacunas(body))
        

        return JsonResponse(res, safe=False)
