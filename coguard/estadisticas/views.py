from dialogflow_fulfillment.rich_responses.payload import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .populate import *
from django.http import JsonResponse
import json

# Create your views here.

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

        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            provincia = body['queryResult']['parameters']['Provincia']
        except Exception as e:
            return JsonResponse({'fulfillmentText': str(e)}, safe=False)

        # Coger el dia mas reciente con estadisticas

        fecha_mas_reciente = EstadisticasTipo1.objects.all().order_by('-fecha_creacion')[0].fecha_creacion

        try:
            informacion_deseada = EstadisticasTipo1.objects.get(fecha_creacion=fecha_mas_reciente, lugar_de_residencia=str(provincia).lower())
        except Exception as e:
            return JsonResponse({'fulfillmentText': str(e)}, safe=False)

        # Comprobar la provincia
        # list_dias_estadisitcas = [{'fecha': str(x.fecha_creacion), 'provincia': x.lugar_de_residencia} for x in EstadisticasTipo1.objects.all()]

        res = "Las estadisticas para la provincia: <b>" + str(provincia) + "</b>, son: \n"
        res += informacion_deseada.parse()

        payload_data = {
            "fulfillmentMessages": [{
                "payload": {
                    "telegram": {
                        "text": res,
                        "parse_mode": "html"
                    }
                },
                "platform": "TELEGRAM"
                }
            ]
        }

        return JsonResponse(payload_data, safe=False)
