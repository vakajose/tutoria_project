import json
import time
def convertir_estructura(datos):
    resultado = []

    # Diccionario para agrupar datos
    agrupado_por_estudiante = {}

    for dato in datos:
        estudiante_id, ci, nombre, apellido_paterno, apellido_materno, periodo, grado, materia, calificacion = dato

        # Verificar si el estudiante ya está en el diccionario
        if estudiante_id not in agrupado_por_estudiante:
            agrupado_por_estudiante[estudiante_id] = {
                "alumno_id": estudiante_id,
                "ci": ci,
                "nombre": nombre,
                "apellido_paterno": apellido_paterno,
                "apellido_materno": apellido_materno,
                "grados": {}
            }

        estudiante = agrupado_por_estudiante[estudiante_id]

        # Verificar si el grado ya está en los datos del estudiante
        if grado not in estudiante["grados"]:
            estudiante["grados"][grado] = {"id": grado, "periodos": {}}

        grado_info = estudiante["grados"][grado]

        # Verificar si el periodo ya está en los datos del grado
        if periodo not in grado_info["periodos"]:
            grado_info["periodos"][periodo] = {"id": periodo, "materias": []}

        periodo_info = grado_info["periodos"][periodo]

        # Añadir la materia y calificación al periodo correspondiente
        periodo_info["materias"].append({"id": materia, "calificacion": calificacion})

    # Convertir el diccionario agrupado en la lista de resultados
    for estudiante_id, estudiante_info in agrupado_por_estudiante.items():
        grados_list = []
        for grado, grado_info in estudiante_info["grados"].items():
            periodos_list = []
            for periodo, periodo_info in grado_info["periodos"].items():
                periodos_list.append(periodo_info)
            grado_info["periodos"] = periodos_list
            grados_list.append(grado_info)
        estudiante_info["grados"] = grados_list
        resultado.append(estudiante_info)

    return resultado

def format_recomends(text):
    # Separar el JSON del texto plano
    json_part = text.split("```json\n")[1].split("```")[0].replace("\n", "")
    plain_text_part = text.split("output_recomendaciones:")[1]

    # Convertir la parte JSON a un diccionario
    json_data = json.loads(json_part)
    
    # Agregar plain_text_part al diccionario JSON
    json_data["recomendaciones"] = plain_text_part
    
    return json_data

def get_time_in_milis():
     return int(time.time() * 1000)