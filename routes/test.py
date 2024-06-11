#from odoo import http 
#from odoo.http import request
import xmlrpc.client

#Datos de conexion
url ='http://localhost:8085'
db = 'odoodb'
username = 'usuario_api'
#password = 'usuario_api'
password = 'b9512b38458fb94db8104d1c1d63fe2728c8b62b'
#class ColegioAPI(http.Controller):
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#print(common.version())

uid = common.authenticate(db, username, password, {})
#print(uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

results = models.execute_kw(db, uid, password, 'ir.model', 'search', [[['model','=','colegio.unidad.educativa']]])
print(results)
result = models.execute_kw(db, uid, password, 'colegio.unidad.educativa', 'get_unidades_educativas', [results])
print(result)


result2 = models.execute_kw(db, uid, password, 'colegio.unidad.educativa', 'read', [[1]], {'fields': ['nombre', 'tipo']})
print(result2)

result3 = models.execute_kw(db, uid, password, 'colegio.unidad.educativa', 'check_access_rights', ['read'], {'raise_exception': False})
print(result3)

result4 = models.execute_kw(db, uid, password, 'colegio.unidad.educativa', 'search', [[['id','=',2]]])
print(result4)

result5 = models.execute_kw(db, uid, password, 'colegio.unidad.educativa', 'search_read', [[]])
print(result5)

result6 = models.execute_kw(db, uid, password, 'colegio.unidad.educativa', 'search_read',[[['id','=',2]]],{'fields': ['nombre', 'tipo']})
print(result6)