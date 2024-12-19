import xmlrpc.client

url = 'http://localhost:8069/'
db = 'db_devBimo18'
username = 'bimo.syahsiraj@gmail.com'
password = '123'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

if uid:
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    partners = models.execute_kw(db,uid,password, 'res.partner', 'search', [[['email', '=', 'bimobaru3@gmail.com']]])

    models.execute_kw(db, uid, password, 'res.partner', 'unlink', [partners])
