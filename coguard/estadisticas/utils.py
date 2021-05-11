from .populate import *
from django.http import JsonResponse


def prettyPrint(msg):

    payload_data = {
        "fulfillmentMessages": [{
            "payload": {
                "telegram": {
                    "text": msg,
                    "parse_mode": "html"
                }
            },
            "platform": "TELEGRAM"
        }
        ]
    }

    return payload_data


def getEstadisticasGenerales(body):

    try:
        lugar_de_residencia = body['queryResult']['parameters']['LugarDeResidencia']
    except Exception as e:
        return JsonResponse({'fulfillmentText': "Error al obtener el lugar de residencia + (" + str(e) + ")"}, safe=False)

    # Coger el dia mas reciente con estadisticas

    fecha_mas_reciente = EstadisticasTipo1.objects.all().order_by('-fecha_creacion')[0].fecha_creacion

    try:
        informacion_deseada = EstadisticasTipo1.objects.get(fecha_creacion=fecha_mas_reciente,
                                                            lugar_de_residencia=str(lugar_de_residencia).lower())
    except Exception as e:
        return JsonResponse({'fulfillmentText': str(e)}, safe=False)

    # Comprobar la provincia
    # list_dias_estadisitcas = [{'fecha': str(x.fecha_creacion), 'provincia': x.lugar_de_residencia} for x in EstadisticasTipo1.objects.all()]

    res = "Las estadisticas para la provincia: <b>" + str(lugar_de_residencia) + "</b>, son: \n"
    res += informacion_deseada.parse()

    return res