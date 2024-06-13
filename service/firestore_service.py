import firebase_admin
from firebase_admin import firestore,credentials
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def init_firebase():
    # Verificar si la app ya ha sido inicializada
    if not firebase_admin._apps:
        # Inicializar Firebase
        cred = credentials.Certificate(os.environ.get('FIREBASE_JSON_NAME'))
        firebase_admin.initialize_app(cred)
    # Obtener una referencia a la base de datos
    return firestore.client()


def save_students(estudiantes):
    # Inicializar cliente de Firestore
    db = init_firebase()
    collect_preffix = os.environ.get('FIREBASE_COLLECTION_PREFIX') or  ""
    # Obtener referencia a la colección
    coleccion_ref = db.collection(collect_preffix + f'_students')

    for estudiante in estudiantes:
        # Crear el documento para el estudiante
        estudiante_ref = coleccion_ref.document(str(estudiante["alumno_id"]))

        # Preparar datos para guardar
        estudiante_data = {
            "alumno_id": estudiante["alumno_id"],
            "nombre": estudiante["nombre"],
            "ci": estudiante["ci"],
            "apellido_paterno": estudiante["apellido_paterno"],
            "apellido_materno": estudiante["apellido_materno"],
            "grados": []
        }

        for grado in estudiante["grados"]:
            grado_data = {
                "id": grado["id"],  # Cambiado a "id"
                "periodos": []
            }
            for periodo in grado["periodos"]:
                periodo_data = {
                    "id": periodo["id"],  # Cambiado a "id"
                    "materias": []
                }
                for materia in periodo["materias"]:
                    materia_data = {
                        "id": materia["id"],  # Cambiado a "id"
                        "calificacion": materia["calificacion"]
                    }
                    periodo_data["materias"].append(materia_data)
                grado_data["periodos"].append(periodo_data)
            estudiante_data["grados"].append(grado_data)

        # Guardar el documento en Firestore
        estudiante_ref.set(estudiante_data)
        print(f"Estudiante {estudiante['nombre']} guardado en Firestore.")


def save_eval(student_id, evals):
    db = init_firebase()
    collect_preffix = os.environ.get('FIREBASE_COLLECTION_PREFIX') or  ""
    # Obtener una referencia al documento del estudiante
    student_ref = db.collection(collect_preffix + f'_students').document(str(student_id))
    # Obtener una referencia a la subcolección 'eval' del estudiante
    eval_ref = student_ref.collection('eval')
    # Guardar la evaluacion en la subcolección 'eval' del estudiante
    eval_ref.add(evals)
    print(f'Evaluacion guardada para el estudiante {student_id}')
