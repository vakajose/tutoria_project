from typing import List, Dict, TypedDict
import typing_extensions as ty

class Materia(ty.TypedDict):
    id: str
    calificacion: float
    def __init__(self, id: str, calificacion: float):
        self.id = id
        self.calificacion = calificacion

class Periodo(ty.TypedDict):
    id: str
    materias: List[Materia]
    def __init__(self, id: str, materias: List[Materia]):
        self.id = id
        self.materias = materias

class Grado(ty.TypedDict):
    id: str
    periodos: List[Periodo]
    def __init__(self, id: str, periodos: List[Periodo]):
        self.id = id
        self.periodos = periodos

class Estudiante(ty.TypedDict):
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


### PROMPT TYPES ###

class Evaluacion(TypedDict):
    pregunta: str
    respuesta: str
    calificacion: str
    
class Cuestionario(TypedDict):
    evaluacion: List[Evaluacion]
    materia: str
    promedio: float

class Diagnostico(TypedDict):
    id: str
    explicacion: str
    cuestionario: List[Cuestionario]
    recomendacion: str
    