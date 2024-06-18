from flask import Flask
from flask_cors import CORS
from routes.api import api_blueprint
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"	}})
# Registro de Blueprint para las rutas de la API
app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(host='0.0.0.0', port=int(os.getenv('FLASK_RUN_PORT', 5000)), debug=debug_mode)
