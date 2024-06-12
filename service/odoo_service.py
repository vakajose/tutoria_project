import xmlrpc.client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#Datos de conexion
url = os.environ.get('ODOO_URL') or 'http://localhost:8069'
db = os.environ.get('ODOO_DB') or 'odoo_db'
username = os.environ.get('ODOO_USERNAME') or 'odoo_db'
password = os.environ.get('ODOO_API_KEY') or 'odoo_db'

def list_all_students_from_odoo():
    #Conexion al servidor
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    print(common.version())

    uid = common.authenticate(db, username, password, {})
    print(uid)

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    model_id = models.execute_kw(db, uid, password, 'ir.model', 'search', [[['model','=','colegios.nota']]])
    print(model_id)
    result = models.execute_kw(db, uid, password, 'colegios.nota', 'consultar_notas', [model_id])
    print(result)
    return result


def get_student_from_odoo(alumno_id:int):
    #Conexion al servidor
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    print(common.version())

    uid = common.authenticate(db, username, password, {})
    print(uid)

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    model_id = models.execute_kw(db, uid, password, 'ir.model', 'search', [[['model','=','colegios.nota']]])
    print(model_id)
    result = models.execute_kw(db, uid, password, 'colegios.nota', 'consultar_notas22', [[model_id],[alumno_id]])
    print(result)
    return result

def login(ci:str, ap:str):
    #Conexion al servidor
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    print(common.version())

    uid = common.authenticate(db, username, password, {})
    print(uid)

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    return models.execute_kw(db, uid, password, 'colegios.alumno', 'search_read',[[['ci','=',ci],['ap_paterno','=',ap]]])


# result6 = models.execute_kw(db, uid, password, 'colegios.alumno', 'search_read',[[['id','=',1]]],{'fields': ['nombres']})
# print(result6)
# result = models.execute_kw(db, uid, password, 'colegios.alumno', 'search_read',[[['ci','=','13204513'],['ap_paterno','=','gutierrez']]])
# print(result)
