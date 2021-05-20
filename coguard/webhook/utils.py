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

def getAyuda():
    res = "Te puedo ofrecer la siguiente información relacionada con la Covid-19:\n"

    res += "\t &#8226; <b>Estadísticas</b>\n"
    res += "\t &#8226; <b>Vacunación</b>\n"
    res += "\t &#8226; <b>Medidas</b>\n"
    
    res += "\nIndícame el tema que te interesa o si quieres conocer todas las ayudas."

    return res

def getAyudaTodo():
    res = "La información disponible es:\n\n"
    
    res += "<b>Estadísticas:</b>\n"
    res += "\t &#8226; Listado de provincias\n"
    res += "\t &#8226; Listado de fechas\n"
    res += "\t &#8226; Tipos de estadísticas\n"
    res += "\t &#8226; Listado de estadísticas generales &lt;provincia&gt; &lt;fecha&gt;\n"
    res += "\t &#8226; Estadísticas &lt;tipo de estadística&gt; &lt;provincia&gt; &lt;fecha&gt;\n"
    res += "\n<b>Vacunación:</b>\n"
    res += "\t &#8226; Listado de vacunas\n"
    res += "\t &#8226; Información general &lt;vacuna&gt;\n"
    res += "\t &#8226; Efectividad &lt;vacuna&gt;\n"
    res += "\t &#8226; Número de dosis &lt;vacuna&gt;\n"
    res += "\t &#8226; Intervalo de dosis &lt;vacuna&gt;\n"
    res += "\t &#8226; Vacuna asignada\n"
    res += "\n<b>Medidas:</b>\n"
    res += "\t &#8226; Listado de fechas con medidas\n"
    res += "\t &#8226; Listado de provincias con medidas\n"
    res += "\t &#8226; Medidias &lt;provincia&gt; &lt;fecha&gt;\n"
    
    return res
