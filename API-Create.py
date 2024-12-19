import xmlrpc.client

url = 'http://localhost:8069/'
db = 'db_devBimo18'
username = 'bimo.syahsiraj@gmail.com'
password = '123'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

if uid:
    print("Authentication succeeded")

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=',True]]], {'limit': 7})

    partners_count = models.execute_kw(db,uid,password, 'res.partner', 'search_count',[[['is_company','=',True]]])

    #read method
    partner_rec = models.execute_kw(db,uid,password,'res.partner','read',[partners],{'fields':['id','name']})

    #search method
    partner_rec2 = models.execute_kw(db,uid,password,'res.partner','search_read',[[['is_company', '=',True]]],{'fields':['id','name']})

# API untuk melakukan CREATE
    vals = {
        'name': 'Bimo baru',
        'email': 'bimobarulagi@gmail.com',
        'vat':'2352125125'
    }

    id = models.execute_kw(db,uid,password, 'res.partner','create',[vals])
else:
     print("Authentication failed")