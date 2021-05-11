from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import *
import json

# Create your views here.

acciones = {
    'ESTADISTICAS GENERALES': 'getEstadisticasGenerales',
}

class PopulateEstadisticasTipo1(APIView):
    def get(self, request):

        prev_estadisticas = len(EstadisticasTipo1.objects.all())
        add_estadisticas_tipo_uno()
        nuevas_estadisticas = len(EstadisticasTipo1.objects.all())

        return Response({"msg": "Se han creado " + str(nuevas_estadisticas - prev_estadisticas) + " estadisticas" }, "200")


class EstadisticasTipo1API(APIView):
    def get(self, request):

        list_dias_estadisitcas = [{'fecha': x.fecha_creacion, 'provincia': str(x.lugar_de_residencia).lower()} for x in EstadisticasTipo1.objects.all()]

        return Response(list_dias_estadisitcas, "200")


class WebhookEstadisticasTipo1API(APIView):
    def post(self, request):

        res = None

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

        return JsonResponse(res, safe=False)
