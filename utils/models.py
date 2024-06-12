from typing import List, Dict

class Materia:
    def __init__(self, id: str, calificacion: int):
        self.id = id
        self.calificacion = calificacion

class Periodo:
    def __init__(self, id: str, materias: List[Materia]):
        self.id = id
        self.materias = materias

class Grado:
    def __init__(self, id: str, periodos: List[Periodo]):
        self.id = id
        self.periodos = periodos

class Estudiante:
    def __init__(self, alumno_id: int, nombre: str, apellido_paterno: str, apellido_materno: str, grados: List[Grado]):
        self.alumno_id = alumno_id
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.grados = grados

def convertir_estructura_tipada(datos) -> List[Estudiante]:
    estudiantes_dict: Dict[int, Estudiante] = {}

    for dato in datos:
        estudiante_id, nombre, apellido_paterno, apellido_materno, periodo, grado, materia, calificacion = dato

        if estudiante_id not in estudiantes_dict:
            estudiantes_dict[estudiante_id] = Estudiante(estudiante_id, nombre, apellido_paterno, apellido_materno, [])

        estudiante = estudiantes_dict[estudiante_id]

        grado_obj = next((g for g in estudiante.grados if g.id == grado), None)
        if not grado_obj:
            grado_obj = Grado(grado, [])
            estudiante.grados.append(grado_obj)

        periodo_obj = next((p for p in grado_obj.periodos if p.id == periodo), None)
        if not periodo_obj:
            periodo_obj = Periodo(periodo, [])
            grado_obj.periodos.append(periodo_obj)

        materia_obj = Materia(materia, calificacion)
        periodo_obj.materias.append(materia_obj)

    return list(estudiantes_dict.values())
