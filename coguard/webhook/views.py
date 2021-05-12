from rest_framework.views import APIView
from django.http import JsonResponse
from estadisticas.utils import getEstadisticasGenerales, getEstadisticasEspecificas, prettyPrint
import json


acciones = {
    'ESTADISTICAS GENERALES': 'getEstadisticasGenerales',
    'ESTADISTICAS ESPECIFICAS': 'getEstadisticasEspecificas',
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

        if action == acciones['ESTADISTICAS GENERALES']:
            res = prettyPrint(getEstadisticasGenerales(body))
        elif action == acciones['ESTADISTICAS ESPECIFICAS']:
            res = prettyPrint(getEstadisticasEspecificas(body))

        return JsonResponse(res, safe=False)
