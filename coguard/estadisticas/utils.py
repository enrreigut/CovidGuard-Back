from .populate import *
from django.http import JsonResponse
import datetime


def getEstadisticasGenerales(body):

    res = ""

    try:
        lugar_de_residencia = body['queryResult']['parameters']['LugarDeResidencia']
    except Exception as e:
        return "Se ha producido un error inesperado. Lo sentimos."

    # Coger fecha

    fecha = get_fecha(body)

    if fecha['texto']:
        res += fecha['texto']
        
    try:
        informacion_deseada = EstadisticasTipo1.objects.get(fecha_creacion=fecha['fecha'],lugar_de_residencia=lugar_de_residencia.lower())
    except Exception as e:
        return "Se ha producido un error inesperado. Lo sentimos."

    res += "Las estadisticas para el lugar de residencia: <b>" + str(lugar_de_residencia) + "</b>, son: \n"
    res += informacion_deseada.parse()

    return res


def getEstadisticasEspecificas(body):

    res = ""

    try:
        lugar_de_residencia = body['queryResult']['parameters']['LugarDeResidencia']
    except Exception as e:
        return "Se ha producido un error inesperado. Lo sentimos."

    try:
        columna = body['queryResult']['parameters']['EstadisticasTipo1']
    except Exception as e:
        return "Se ha producido un error inesperado. Lo sentimos."

    # Coger fecha

    fecha = get_fecha(body)

    if fecha['texto']:
        res += fecha['texto']

    try:
        informacion_deseada = getattr(EstadisticasTipo1.objects.get(fecha_creacion=fecha['fecha'],
                                                                    lugar_de_residencia=str(lugar_de_residencia).lower()), columna)
    except Exception as e:
        return "Se ha producido un error inesperado. Lo sentimos."

    res += "El atributo <b>'" + columna + "'</b> para <b>" + str(lugar_de_residencia) + "</b> el <b>" + str(fecha['fecha']) + "</b>, es de <b>" + str(informacion_deseada) + "</b>\n"

    return res


def getFechasEstadisticas():

    fechas = EstadisticasTipo1.objects.values('fecha_creacion').distinct()

    res = "Las fechas con estadísticas son: \n"
    for fecha in fechas:
        
        fecha = fecha['fecha_creacion'].strftime("%d-%m-%Y")
        res += "&#8226; <b>" + fecha + "</b>\n"

    return res


def getAyudaEstadisticas():
    res = "La información disponible de <b>Estadísticas</b> es:\n"

    res += "\t &#8226; Listado de lugares de residencia\n"
    res += "\t &#8226; Listado de fechas con estadísticas\n"
    res += "\t &#8226; Tipos de estadísticas\n"
    res += "\t &#8226; Listado de estadísticas generales &lt;provincia&gt; &lt;fecha&gt;\n"
    res += "\t &#8226; Estadísticas &lt;tipo de estadística&gt; &lt;provincia&gt; &lt;fecha&gt;\n"

    return res


def getTipoEstadisticas():

    fields = EstadisticasTipo1._meta.get_fields()
    res = "Los <b>tipos de estadísticas</b> registrados son:\n"
    for field in fields:
        if field.name != "id":
            res += "&#8226; <b>" + str(field.name) + "</b>\n"

    return res


# Utilidades

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))


def get_fecha(body):

    texto_adicional = None

    try:
        print(body['queryResult']['parameters']['date'])
        fecha_body = datetime.datetime.strptime(body['queryResult']['parameters']['date'], "%Y-%m-%dT%H:%M:%S%z").date()

        fecha = fecha_body if len(EstadisticasTipo1.objects.filter(fecha_creacion=fecha_body)) > 0 else None

        if not fecha:
            fecha = nearest([x.fecha_creacion for x in EstadisticasTipo1.objects.all()], fecha_body)
            texto_adicional = "No se encuentra la fecha indicada (<b>" + str(fecha_body) + "</b>). Se ha aproximado a la más cercana: <b>" + str(fecha) + "</b>\n"

    except Exception as e:
        fecha = EstadisticasTipo1.objects.all().order_by('-fecha_creacion')[0].fecha_creacion

    return {'fecha': fecha, 'texto': texto_adicional}
