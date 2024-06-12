from flask import Blueprint, request, jsonify
from service import odoo_service,firestore_service
from utils import utils

api_blueprint = Blueprint('api', __name__)

#firebase api AIzaSyBVQTcUPcUg1128L_BbeVDsyhsYiLpxsVs


@api_blueprint.route('/init_recomendaciones/<int:id_estudiante>', methods=['GET'])
def iniciar_recomendaciones(id_estudiante: int):
    #consultar a odoo la informacion del estudiante
    students = odoo_service.get_student_from_odoo(id_estudiante)
    grouped = utils.convertir_estructura(students)

    #guardar estudiantes en firebase
    firestore_service.save_students(grouped)

    #generar cuestionario de evaluacion en google ai studio
    #guardar cuestionario en firebase
    #retornar cuestionario juntos con los datos del estudiante al frontend
    
    return jsonify(grouped),200
   



@api_blueprint.route('/evaluaciones', methods=['POST'])
def recibir_evaluacion():
    data = request.get_json()
    alumno_id = data.get('alumno_id')
    resultados = data.get('resultados')

#     # Almacenar en Firebase Firestore
#     evaluacion_ref = db.collection('evaluaciones').document()
#     evaluacion_ref.set({
#         'id_estudiante': id_estudiante,
#         'resultados': resultados,
#         'fecha': firestore.SERVER_TIMESTAMP
#     })

#     #Generar recomendaciones usando Google Generative AI
#     recomendaciones = generate_recommendations(resultados)
#     recomendacion_ref = db.collection('recomendaciones').document()
#     recomendacion_ref.set({
#         'id_estudiante': id_estudiante,
#         'recomendaciones': recomendaciones,
#         'fecha': firestore.SERVER_TIMESTAMP
#     })

#     return jsonify({'status': 'success', 'recomendaciones': recomendaciones})



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