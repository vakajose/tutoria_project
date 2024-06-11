from flask import Flask
from routes.api import api_blueprint
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Inicializar Firebase
cred = credentials.Certificate('toturia-firebase-adminsdk-c8g2u-6343d912fb.json')
firebase_admin.initialize_app(cred)

# Crear una referencia a la base de datos
db = firestore.client()

# Registro de Blueprint para las rutas de la API
app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
