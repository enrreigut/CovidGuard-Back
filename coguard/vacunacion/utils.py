from .models import *


def getEfectividadVacuna(body):
    
    res = "Depende de la vacuna que te interese. ¿Quieres conocer el listado?"
    
    nombreVacuna = body['queryResult']['parameters']['Vacuna']
    
    if nombreVacuna:
        vacuna = Vacuna.objects.get(nombre=nombreVacuna)
        segunda_dosis_info = " después de la segunda dosis." if vacuna.numero_de_dosis > 1 else "."
        apodo = " (" + vacuna.apodo + ")" if vacuna.apodo is not None else ""
        res = "La vacuna <b>" + str(vacuna) + apodo + "</b> es efectiva tras " + str(vacuna.dias_hasta_efectividad) + " dias" + segunda_dosis_info

    return res

def getNumeroDosisVacuna(body):
    
    res = "Depende de la vacuna que te interese. ¿Quieres conocer el listado?"

    nombreVacuna = body['queryResult']['parameters']['Vacuna']
    
    if nombreVacuna:
        vacuna = Vacuna.objects.get(nombre=nombreVacuna)
        apodo = " (" + vacuna.apodo + ")" if vacuna.apodo is not None else ""
        res = "La vacuna <b>" + str(vacuna) + apodo + "</b> requiere actualmente de " + str(vacuna.numero_de_dosis) + " dosis."

    return res

def getIntervaloDosisVacuna(body):
    
    res = "Depende de la vacuna que te interese. ¿Quieres conocer el listado?"
    
    nombreVacuna = body['queryResult']['parameters']['Vacuna']
    
    if nombreVacuna:
        vacuna = Vacuna.objects.get(nombre=nombreVacuna)
        apodo = " (" + vacuna.apodo + ")" if vacuna.apodo is not None else ""
        
        if vacuna.numero_de_dosis > 1:
            res = "La segunda dosis de la vacuna <b>" + str(vacuna) + apodo + "</b> se suministra " + vacuna.intervalo_dosis + " después de la primera."
        else:
            res = "La vacuna <b>" + str(vacuna) + "</b> requiere de una única dosis."

    return res


def getInfoGeneralVacuna(body):
    
    res = "Depende de la vacuna que te interese. ¿Quieres conocer el listado?"
    
    nombreVacuna = body['queryResult']['parameters']['Vacuna']
    
    if nombreVacuna:
        vacuna = Vacuna.objects.get(nombre=nombreVacuna)
        segunda_dosis_info = " después de la segunda dosis." if vacuna.numero_de_dosis > 1 else "."
        apodo = " (" + vacuna.apodo + ")" if vacuna.apodo is not None else ""
        
        res = "Tengo los siguientes datos de <b>" + str(vacuna) + apodo + "</b>:\n"
        
        if vacuna.numero_de_dosis > 1:
            res += "&#8226; Requiere de <b>" + str(vacuna.numero_de_dosis) + " dosis</b>\n"
            res += "&#8226; La segunda dosis se administra <b>" + vacuna.intervalo_dosis + " </b>después de la primera.\n"
        else:
            res += "&#8226; Requiere de <b>" + str(vacuna.numero_de_dosis) + " dosis</b>\n"
            
        
        res += "&#8226; Es efectiva tras <b>" + str(vacuna.dias_hasta_efectividad) + " días</b>" + segunda_dosis_info

    return res

def getListadoVacunas(body):
    
    res = "Las <b>vacunas</b> disponibles son:\n"
    
    vacunas = Vacuna.objects.all()
    
    for vacuna in vacunas:
        
        if vacuna.apodo is not None:
            res += "&#8226; <b>" + vacuna.nombre + " (" + vacuna.apodo + ")</b>\n"
        else:
            res += "&#8226; <b>" + vacuna.nombre + "</b>\n"
            
    res += "\n¿Cuál te interesa?"
            
    return res

def getVacunaPorEdad(body):
    
    res = "No hay aún una vacuna asignada para ti."
    
    anyoNacimiento = body['queryResult']['parameters']['AnyoNacimiento']
    
    if anyoNacimiento < 1880 or anyoNacimiento > 2025:
        res = "El año introducido no es válido"
        
    else:
        tipo_vacuna = IntervaloEdad.objects.filter(inicio__lte=anyoNacimiento,fin__gte=anyoNacimiento)[0].tipo_de_vacuna
        tipo_vacuna = tipo_vacuna.replace('break','\n')
    
        if tipo_vacuna != "Por determinar":
            res = "En ese caso, te corresponderá:\n" + tipo_vacuna
    
    return res

def getAyudaVacunacion():
    res = "La información disponible de <b>Vacunación</b> es:\n"

    res += "\t &#8226; Listado de vacunas\n"
    res += "\t &#8226; Información general &lt;vacuna&gt;\n"
    res += "\t &#8226; Efectividad &lt;vacuna&gt;\n"
    res += "\t &#8226; Número de dosis &lt;vacuna&gt;\n"
    res += "\t &#8226; Intervalo de dosis &lt;vacuna&gt;\n"
    res += "\t &#8226; Vacuna asignada"

    return res
