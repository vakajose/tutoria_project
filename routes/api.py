from flask import Blueprint, request, jsonify
from service import odoo_service,firestore_service,ai_service
from utils import utils
from utils import models
import json

api_blueprint = Blueprint('api', __name__)

#firebase api AIzaSyBVQTcUPcUg1128L_BbeVDsyhsYiLpxsVs


@api_blueprint.route('/init_recomendaciones/<int:id_estudiante>', methods=['GET'])
def iniciar_recomendaciones(id_estudiante: int):
    #consultar a odoo la informacion del estudiante
    students = odoo_service.get_student_from_odoo(id_estudiante)
    grouped = utils.convertir_estructura(students)

#     grouped = [
#     {
#         "alumno_id": 1,
#         "apellido_materno": "Fernandez",
#         "apellido_paterno": "Vaca",
#         "ci": "4362575",
#         "grados": [
#             {
#                 "id": "1 secundaria",
#                 "periodos": [
#                     {
#                         "id": "1-2022",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 30
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 55
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 70
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 85
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 90
#                             }
#                         ]
#                     },
#                     {
#                         "id": "2-2022",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 40
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 60
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 75
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 88
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 92
#                             }
#                         ]
#                     },
#                     {
#                         "id": "3-2022",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 50
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 65
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 80
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 90
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 95
#                             }
#                         ]
#                     }
#                 ]
#             },
#             {
#                 "id": "2 secundaria",
#                 "periodos": [
#                     {
#                         "id": "1-2023",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 60
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 70
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 85
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 75
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 80
#                             }
#                         ]
#                     },
#                     {
#                         "id": "2-2023",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 65
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 75
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 88
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 78
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 85
#                             }
#                         ]
#                     },
#                     {
#                         "id": "3-2023",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 70
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 80
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 90
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 82
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 88
#                             }
#                         ]
#                     }
#                 ]
#             },
#             {
#                 "id": "3 secundaria",
#                 "periodos": [
#                     {
#                         "id": "1-2024",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 75
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 85
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 92
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 88
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 90
#                             }
#                         ]
#                     },
#                     {
#                         "id": "2-2024",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 80
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 88
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 94
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 90
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 92
#                             }
#                         ]
#                     },
#                     {
#                         "id": "3-2024",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 85
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 90
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 95
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 92
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 94
#                             }
#                         ]
#                     }
#                 ]
#             },
#             {
#                 "id": "4 secundaria",
#                 "periodos": [
#                     {
#                         "id": "1-2025",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 90
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 92
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 94
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 91
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 93
#                             }
#                         ]
#                     },
#                     {
#                         "id": "2-2025",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 91
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 93
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 95
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 92
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 94
#                             }
#                         ]
#                     },
#                     {
#                         "id": "3-2025",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 92
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 94
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 96
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 93
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 95
#                             }
#                         ]
#                     }
#                 ]
#             },
#             {
#                 "id": "5 secundaria",
#                 "periodos": [
#                     {
#                         "id": "1-2026",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 93
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 95
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 97
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 94
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 96
#                             }
#                         ]
#                     },
#                     {
#                         "id": "2-2026",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 94
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 96
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 98
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 95
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 97
#                             }
#                         ]
#                     },
#                     {
#                         "id": "3-2026",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 95
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 97
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 99
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 96
                           

#  },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 98
#                             }
#                         ]
#                     }
#                 ]
#             },
#             {
#                 "id": "6 secundaria",
#                 "periodos": [
#                     {
#                         "id": "1-2027",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 96
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 98
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 99
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 97
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 99
#                             }
#                         ]
#                     },
#                     {
#                         "id": "2-2027",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 97
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 99
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 100
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 98
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 100
#                             }
#                         ]
#                     },
#                     {
#                         "id": "3-2027",
#                         "materias": [
#                             {
#                                 "id": "matematicas",
#                                 "calificacion": 98
#                             },
#                             {
#                                 "id": "ingles",
#                                 "calificacion": 100
#                             },
#                             {
#                                 "id": "lenguaje",
#                                 "calificacion": 100
#                             },
#                             {
#                                 "id": "ciencias",
#                                 "calificacion": 99
#                             },
#                             {
#                                 "id": "educacion_fisica",
#                                 "calificacion": 100
#                             }
#                         ]
#                     }
#                 ]
#             }
#         ],
#         "nombre": "Jose Luis"
#     }
# ]

    #guardar estudiantes en firebase
    firestore_service.save_students(grouped)

    #generar cuestionario de evaluacion en google ai studio
    result = ai_service.get_eval(grouped[0].get('grados'))
    #asignar id
    result['id'] = str(utils.get_time_in_milis())
    #guardar cuestionario en firebase
    firestore_service.save_eval(student_id=id_estudiante,eval=result)

    return jsonify(result),200
   



@api_blueprint.route('/evaluaciones_old', methods=['POST'])
def recibir_evaluacion():
    data = request.get_json()
    alumno_id = data.get('alumno_id')
    respuestas = data.get('respuestas')
    
    #obtener datos del estudiante desde firebase
    estudiante = firestore_service.get_student(alumno_id)
    if estudiante is not None:
        grados = estudiante['grados']
        id = respuestas['id']
        result = ai_service.get_recomends(grados,respuestas)
        formated = utils.format_recomends(result)
        
        #guardar el formatted en  firebase como parte de la subcoleccion evals del estudiante
        firestore_service.save_recomends(alumno_id,formated,id)
        
        return jsonify({'status': 'success', 'recomendaciones': formated}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Estudiante no encontrado'}), 404
    
    
@api_blueprint.route('/evaluaciones', methods=['POST'])
def recibir_evaluacion_json():
    data = request.get_json()
    print(f'___________________________REQUEST_____________________________')
    print(json.dumps(data, indent=4, ensure_ascii=False))
    alumno_id = data.get('alumno_id')
    respuestas = data.get('respuestas')
    
    #obtener datos del estudiante desde firebase
    estudiante = firestore_service.get_student(alumno_id)
    if estudiante is not None:
        grados = estudiante['grados']
        id = respuestas['id']
        result = ai_service.get_recomends_json(grados,respuestas)
        
        diagnostico : models.Diagnostico = json.loads(result)
        
        #guardar el formatted en  firebase como parte de la subcoleccion evals del estudiante
        firestore_service.save_recomends(alumno_id,diagnostico,id)
        print(f'___________________________FORMATED_____________________________')
        print(json.dumps(diagnostico, indent=4, ensure_ascii=False))
        return jsonify({'status': 'success', 'recomendaciones': diagnostico}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Estudiante no encontrado'}), 404



@api_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    ci = data.get('ci')
    apellido = data.get('apellido')
    result = odoo_service.login(ci=ci,ap=apellido)
    print(len(result))
    if len(result)<=0:
        return jsonify({'status': 'error', 'message': 'Resource not found'}), 404
    else:
        return jsonify({'status': 'success', 'alumno': result}) , 200


@api_blueprint.route('/test/<test>', methods=['GET'])
def test(test):
    # Obtener recomendaciones desde Firebase Firestore
    mensaje =  f'Hola probando servicio: {test}'
    return jsonify({'mensaje': mensaje}) , 200