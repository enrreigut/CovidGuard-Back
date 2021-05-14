from rest_framework.views import APIView
from django.http import JsonResponse
from estadisticas.utils import *
import json


acciones = {
    'AYUDAS': 'getAyudas',
    'ESTADISTICAS FECHAS': 'getEstadisticasFechas',
    'ESTADISTICAS TIPOS': 'getTiposEstadisticas',
    'ESTADISTICAS GENERALES': 'getEstadisticasGenerales',
    'ESTADISTICAS ESPECIFICAS': 'getEstadisticasEspecificas'
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

        return JsonResponse(res, safe=False)
