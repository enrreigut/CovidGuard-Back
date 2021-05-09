from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .populate import *


# Create your views here.
class EstadisticasTipo1API(APIView):
    def get(self, request):

        list_dias_estadisitcas = [{'fecha': x.fecha_creacion, 'provincia': x.lugar_de_residencia} for x in EstadisticasTipo1.objects.all()]

        return Response(list_dias_estadisitcas, "200")
