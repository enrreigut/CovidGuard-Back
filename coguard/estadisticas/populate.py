from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
from django.db import IntegrityError
from .models import *
from datetime import datetime
from django.utils import timezone
import requests


def update_estadistica_tipo_uno(estadistica_actual, nueva_estadistica):

    nueva_estadistica.id = estadistica_actual.id
    estadistica_actual = nueva_estadistica

    estadistica_actual.save()


def get_response(url):
    url = "https://www.juntadeandalucia.es/institutodeestadisticaycartografia/intranet/admin/rest/v1.0/consulta/44088"
    res = requests.get(url)

    if res.status_code != 200:
        return None

    return res.json()


def create_estadisticas_tipo_uno():

    url = "https://www.juntadeandalucia.es/institutodeestadisticaycartografia/intranet/admin/rest/v1.0/consulta/44088"
    estadisticas = get_response(url)

    if estadisticas is None:
        return None

    estadisticas_totales = []
    for provincia in estadisticas['data']:
        estadisticas_provincia = EstadisticasTipo1(
            fecha_creacion=timezone.now().date(),
            lugar_de_residencia=provincia[0]['des'],
            total_confirmados=int(float(provincia[1]['val'])),
            tasa_total_confirmados=float(provincia[2]['val']),
            confirmados_PDIA=int(float(provincia[3]['val'])),
            tasa_PDIA=float(provincia[4]['val']),
            confirmados_PDIA_14=int(float(provincia[5]['val'])),
            tasa_PDIA_14=float(provincia[6]['val']),
            confirmados_PDIA_7=int(float(provincia[7]['val'])),
            tasa_PDIA_7=float(provincia[8]['val']),
            curados=int(float(provincia[9]['val'])),
            fallecidos=int(float(provincia[10]['val']))
        )

        estadisticas_totales.append(estadisticas_provincia)

    return estadisticas_totales


def check_if_equals(estadistica, nueva_estadistica):

    if estadistica.lugar_de_residencia != nueva_estadistica.lugar_de_residencia:
        return False

    if estadistica.total_confirmados != nueva_estadistica.total_confirmados:
        return False

    if estadistica.tasa_total_confirmados != nueva_estadistica.tasa_total_confirmados:
        return False

    if estadistica.confirmados_PDIA != nueva_estadistica.confirmados_PDIA:
        return False

    if estadistica.tasa_PDIA != nueva_estadistica.tasa_PDIA:
        return False

    if estadistica.confirmados_PDIA_14 != nueva_estadistica.confirmados_PDIA_14:
        return False

    if estadistica.tasa_PDIA_14 != nueva_estadistica.tasa_PDIA_14:
        return False

    if estadistica.confirmados_PDIA_7 != nueva_estadistica.confirmados_PDIA_7:
        return False

    if estadistica.tasa_PDIA_7 != nueva_estadistica.tasa_PDIA_7:
        return False

    if estadistica.curados != nueva_estadistica.curados:
        return False

    if estadistica.fallecidos != nueva_estadistica.fallecidos:
        return False

    return True


def add_estadisticas_tipo_uno():

    # Si existen valores comprobar que:
    #   - Si la fecha coincide con la del momento de añadir:
    #       - Comprobar que los valores son distintos
    #           - Si lo son sobreescribir
    #           - En caso contrario no hacer nada
    #       - En caso contrario como las fechas no coinciden crear una nueva entrada

    nuevas_estadisticas = create_estadisticas_tipo_uno()
    estadisticas = EstadisticasTipo1.objects.all()

    if len(estadisticas) > 0:
        for estadistica in estadisticas:
            for nueva_estadistica in nuevas_estadisticas:
                if estadistica.lugar_de_residencia == nueva_estadistica.lugar_de_residencia:
                    if estadistica.fecha_creacion != nueva_estadistica.fecha_creacion:
                        nueva_estadistica.save()
                    else:
                        if not check_if_equals(estadistica, nueva_estadistica):
                            print("update")
                            update_estadistica_tipo_uno(estadistica, nueva_estadistica)
    else:
        EstadisticasTipo1.objects.bulk_create(nuevas_estadisticas)
