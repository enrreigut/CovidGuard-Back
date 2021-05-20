from .models import *
import datetime
from django.http import JsonResponse


def getMedidasFechas():
    fechas = Medidas.objects.values('fecha_creacion').distinct()

    res = "Las fechas con medidas son: \n"
    for fecha in fechas:
        res += "<b>&#8226;" + str(fecha['fecha_creacion']) + "</b>\n"

    return res


def getMedidasProvincias():
    provincias = Medidas.objects.values('provincia').distinct()

    res = "Las medidas con provincias son: \n"
    for provincia in provincias:
        res += "> <b>" + str(provincia['provincia']) + "</b>\n"

    return res


def getMedidasEspecificas(body):
    res = ""

    try:
        provincia = body['queryResult']['parameters']['LugarDeResidencia']
    except Exception as e:
        return JsonResponse({'fulfillmentText': "Error al obtener el lugar de residencia + (" + str(e) + ")"},
                            safe=False)

    # Coger fecha

    fecha = get_fecha(body)

    if fecha['texto']:
        res += fecha['texto']

    try:
        informacion_deseada = Medidas.objects.get(provincia=provincia)

    except Exception as e:
        return JsonResponse({'fulfillmentText': str(e)}, safe=False)

    res += "Las médidias para <b>" + str(provincia) + "</b> el <b>" + str(fecha['fecha']) + "</b>, son:\n"

    res += "<b>Nivel de restricción</b>: " + get_nivel(str(informacion_deseada.nivel)) + "\n"

    if informacion_deseada.cierre_perimetral:
        res += "<b>Cierre perimetral</b>: Sí\n\n"
    else:
        res += "<b>Cierre perimetral</b>: No\n\n"

    if informacion_deseada.horarios_ocio_nocturno != 'N':
        res += "<b>OCIO NOCTURNO</b>:" +"\n\n"
        res += "<b>&#8226; Horario de cierre</b>: " + str(informacion_deseada.horarios_ocio_nocturno) + "\n"

        if informacion_deseada.aforo_ocio_nocturno_exterior is None:
            res += "<b>&#8226; Número de personas en terraza/exterior</b>: No se indica" + "\n"
        else:
            res += "<b>&#8226; Número de personas en terraza/exterior</b>:" + str(informacion_deseada.aforo_ocio_nocturno_exterior) + "\n"

        if informacion_deseada.aforo_ocio_nocturno_interior is None:
            res += "<b>&#8226; Número de personas en interior</b>: No se indica" + "\n"
        else:
            res += "<b>&#8226; Número de personas en terraza/exterior</b>:" + str(informacion_deseada.aforo_ocio_nocturno_interior) + "\n"

    res += "\n<b>HOSTELERÍA</b>:\n\n"
    res += "<b>&#8226; Horario de cierre</b>: " + str(informacion_deseada.horario_hosteleria) + "\n"

    if informacion_deseada.aforo_hosteleria_nocturno_exterior is None:
        res += "<b>&#8226; Número de personas en terraza/exterior</b>: No se indica" + "\n"
    else:
        res += "<b>&#8226; Número de personas en terraza/exterior</b>:" + str(
            informacion_deseada.aforo_hosteleria_nocturno_exterior) + "\n"

    if informacion_deseada.aforo_hosteleria_nocturno_interior is None:
        res += "<b>&#8226; Número de personas en interior</b>: No se indica" + "\n"
    else:
        res += "<b>&#8226; Número de personas en terraza/exterior</b>:" + str(
            informacion_deseada.aforo_hosteleria_nocturno_interior) + "\n"

    return res


# Utilidades

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))


def get_fecha(body):

    texto_adicional = None

    try:
        fecha_body = datetime.datetime.strptime(body['queryResult']['parameters']['date'], "%Y-%m-%dT%H:%M:%S%z").date()

        print(fecha_body)

        fecha = fecha_body if len(Medidas.objects.filter(fecha_creacion=fecha_body)) > 0 else None

        if not fecha:
            fecha = nearest([x.fecha_creacion for x in Medidas.objects.all()], fecha_body)
            texto_adicional = "No se encuentra la fecha indicada (<b>" + str(fecha_body) + "</b>). Se ha aproximado a la más cercana: <b>" + str(fecha) + "</b>\n"

    except Exception as e:
        fecha = Medidas.objects.all().order_by('-fecha_creacion')[0].fecha_creacion

    return {'fecha': fecha, 'texto': texto_adicional}


def get_nivel(nivel):
    if nivel == "0":
        return "Sin Alerta"
    elif nivel == "5":
        return "4 (I)"
    elif nivel == "6":
        return "4 (II)"
    else:
        return nivel
