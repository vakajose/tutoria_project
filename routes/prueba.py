import xmlrpc.client

#Datos de conexion
url ='http://192.168.3.69:8085'
db = 'odooExamen'
username = 'usuario_api'
#password = 'usuario_api'
password = '5362fc5061dd406b74b55be9dd640faa5cc45084'
#class ColegioAPI(http.Controller):
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# result6 = models.execute_kw(db, uid, password, 'colegios.alumno', 'search_read',[[['id','=',1]]],{'fields': ['nombres']})
# print(result6)

# result = models.execute_kw(db, uid, password, 'colegios.alumno', 'search_read',[[['ci','=','13204513'],['ap_paterno','=','gutierrez']]])
# print(result)

resultado1 = models.execute_kw(db, uid, password, 'ir.model', 'search', [[['model','=','colegios.nota']]])
print(resultado1)
resutlado2 = models.execute_kw(db, uid, password, 'colegios.nota', 'consultar_notas', [resultado1])
print(resutlado2)
