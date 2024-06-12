import xmlrpc.client

#Datos de conexion
url ='http://192.168.3.69:8085'
db = 'odooExamen'
username = 'usuario_api'
#password = 'usuario_api'
password = '5362fc5061dd406b74b55be9dd640faa5cc45084'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

model_id = models.execute_kw(db, uid, password, 'ir.model', 'search', [[['model','=','colegios.nota']]])
print(model_id)
# result = models.execute_kw(db, uid, password, 'colegios.nota', 'consultar_notas', [model_id])
# print(result)

result2 = models.execute_kw(db, uid, password, 'colegios.nota', 'consultar_notas22', [[model_id],[1]])
print(result2)


# result6 = models.execute_kw(db, uid, password, 'colegios.alumno', 'search_read',[[['id','=',1]]],{'fields': ['nombres']})
# print(result6)
# result = models.execute_kw(db, uid, password, 'colegios.alumno', 'search_read',[[['ci','=','13204513'],['ap_paterno','=','gutierrez']]])
# print(result)
