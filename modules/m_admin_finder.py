import requests as r
from time import sleep

endpoints = [
    'admin', 'administrator', 'wp-admin', 'login.php', 'auth',
    'login', 'login.aspx', 'admin.php', 'admin.aspx',
    'admin/login', 'panel'
]

def find_admin(domain):
    results = {}
    
    for page in endpoints:
        try:
            address = "{}/{}".format(domain, page)
            
            tls = r.get("http://" + address)
            
            if tls.status_code == 200 or tls.status_code == 403:
                results[page] = True
        except:
            results[page] = False
    
    return results