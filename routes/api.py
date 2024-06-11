from flask import Blueprint, request, jsonify
#from models.model import generate_recommendations
#from app import db
from firebase_admin import credentials, firestore

api_blueprint = Blueprint('api', __name__)

#firebase api AIzaSyBVQTcUPcUg1128L_BbeVDsyhsYiLpxsVs

@api_blueprint.route('/evaluaciones', methods=['POST'])
def recibir_evaluacion():
    data = request.get_json()
#     id_estudiante = data.get('id_estudiante')
#     resultados = data.get('resultados')

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

@api_blueprint.route('/init_recomendaciones/<int:id_estudiante>', methods=['GET'])
def iniciar_recomendaciones(id_estudiante):
    mensaje = f'hola mundo'
#     # Obtener recomendaciones desde Firebase Firestore
#     recomendaciones_ref = db.collection('recomendaciones').where('id_estudiante', '==', id_estudiante)
#     recomendaciones = [doc.to_dict() for doc in recomendaciones_ref.stream()]
#     return jsonify({'recomendaciones': recomendaciones})


@api_blueprint.route('/test/<test>', methods=['GET'])
def test(test):
    # Obtener recomendaciones desde Firebase Firestore
    mensaje =  f'Hola probando servicio: {test}'
    return jsonify({'mensaje': mensaje})