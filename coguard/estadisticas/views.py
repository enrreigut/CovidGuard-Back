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

        list_dias_estadisitcas = [{'fecha': x.fecha_creacion, 'provincia': x.lugar_de_residencia} for x in EstadisticasTipo1.objects.all()]

        return Response(list_dias_estadisitcas, "200")


class WebhookEstadisticasTipo1API(APIView):
    def post(self, request):
        list_dias_estadisitcas = [{'fecha': str(x.fecha_creacion), 'provincia': x.lugar_de_residencia} for x in EstadisticasTipo1.objects.all()]

        return JsonResponse(list_dias_estadisitcas, safe=False)
