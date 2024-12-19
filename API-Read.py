import xmlrpc.client

url = 'http://localhost:8069/'
db = 'db_devBimo18'
username = 'bimo.syahsiraj@gmail.com'
password = '123'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

if uid:
    print("Authentication succeeded")
else:
     print("Authentication failed")

# API untuk read & search

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# search method
partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])

print("------>",partners)


partner_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners], {'fields': ['name', 'id']})
print("------->", partner_rec)