from .populate import *
from django.http import JsonResponse
import datetime


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
        }]
    }

    return payload_data


def getEstadisticasGenerales(body):

    res = ""

    try:
        lugar_de_residencia = body['queryResult']['parameters']['LugarDeResidencia']
    except Exception as e:
        return JsonResponse({'fulfillmentText': "Error al obtener el lugar de residencia + (" + str(e) + ")"},
                            safe=False)

    # Coger fecha

    fecha = get_fecha(body)

    if fecha['texto']:
        res += fecha['texto']

    try:
        informacion_deseada = EstadisticasTipo1.objects.get(fecha_creacion=fecha['fecha'],
                                                            lugar_de_residencia=str(lugar_de_residencia).lower())
    except Exception as e:
        return JsonResponse({'fulfillmentText': str(e)}, safe=False)

    res += "Las estadisticas para el lugar de residencia: <b>" + str(lugar_de_residencia) + "</b>, son: \n"
    res += informacion_deseada.parse()

    return res


def getEstadisticasEspecificas(body):

    res = ""

    try:
        lugar_de_residencia = body['queryResult']['parameters']['LugarDeResidencia']
    except Exception as e:
        return JsonResponse({'fulfillmentText': "Error al obtener el lugar de residencia + (" + str(e) + ")"},
                            safe=False)

    try:
        columna = body['queryResult']['parameters']['EstadisticasTipo1']
    except Exception as e:
        return JsonResponse({'fulfillmentText': "Error al obtener el lugar de residencia + (" + str(e) + ")"},
                            safe=False)

    # Coger fecha

    fecha = get_fecha(body)

    if fecha['texto']:
        res += fecha['texto']

    try:
        informacion_deseada = getattr(EstadisticasTipo1.objects.get(fecha_creacion=fecha['fecha'],
                                                                    lugar_de_residencia=str(lugar_de_residencia).lower()), columna)
    except Exception as e:
        return JsonResponse({'fulfillmentText': str(e)}, safe=False)

    res += "El atributo <b>'" + columna + "'</b> para <b>" + str(lugar_de_residencia) + "</b> el <b>" + \
          str(fecha['fecha']) + "</b>, es de <b>" + str(informacion_deseada) + "</b>\n"

    return res


def getFechasEstadisticas():

    fechas = EstadisticasTipo1.objects.values_list('fecha_creacion').distinct()

    res = "Las fechas con estadísticas son: \n"
    for fecha in fechas:
        res += "> <b>" + str(fecha) + "</b>\n"

    return res


def getAyudas():
    res = """Esto son las cosas de las que te puedo dar informacion:
    <b>Estadísitcas:</b>
        Listado de provincias con estadísticas
        Listado de fechas con estadísticas
        Listado de estadísticas
        Listado de estadísticas generales <provincia> <fecha>
        Listado de estadísticas específicas <provincia> <fecha>"""

    return res

# Utilidades

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))


def get_fecha(body):

    texto_adicional = None

    try:
        fecha_body = datetime.datetime.strptime(body['queryResult']['parameters']['date'], "%Y-%m-%dT%H:%M:%S%z").date()

        print(fecha_body)

        fecha = fecha_body if len(EstadisticasTipo1.objects.filter(fecha_creacion=fecha_body)) > 0 else None

        if not fecha:
            fecha = nearest([x.fecha_creacion for x in EstadisticasTipo1.objects.all()], fecha_body)
            texto_adicional = "No se encuentra la fecha indicada (<b>" + str(fecha_body) + "</b>). Se ha aproximado a la más cercana: <b>" + str(fecha) + "</b>\n"

    except Exception as e:
        fecha = EstadisticasTipo1.objects.all().order_by('-fecha_creacion')[0].fecha_creacion

    return {'fecha': fecha, 'texto': texto_adicional}
