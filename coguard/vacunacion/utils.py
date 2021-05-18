from .models import Vacuna


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

def getListadoVacunas(body):
    
    res = "Las <b>vacunas</b> disponibles son:\n"
    
    vacunas = Vacuna.objects.all()
    
    for vacuna in vacunas:
        
        if vacuna.apodo is not None:
            res += "&gt <b>" + vacuna.nombre + " (" + vacuna.apodo + ")</b>\n"
        else:
            res += "&gt <b>" + vacuna.nombre + "</b>\n"
            
    res += "\n¿Cuál te interesa?"
            
    return res
        