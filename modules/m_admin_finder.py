import requests as r
from os import getcwd, sep

filePath = getcwd()+sep+"extra"+sep+"acp.txt"
endpoints = open(filePath, "r").readlines()

def find_admin(domain):
    results = {}

    for page in endpoints:
        page = page.split()[0]
        con = 0
        try:
            address = "{}/{}".format(domain, page)

            tls = r.get("http://" + address)

            if tls.status_code == 200 or tls.status_code == 403:
                results[page] = True
                con = 1
                break
        except:
            pass

    if con != 1: results[page] = False
    return results
