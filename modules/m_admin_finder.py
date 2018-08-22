import os, requests

file_path = os.path.join(os.path.dirname(__file__), '..', 'extra', 'acp.txt')
endpoints = map(lambda x: x.strip(), open(file_path, 'r').readlines())

def find_admin(domain):
    for panel in endpoints:
        request_url = 'http://' + '/'.join([domain, panel.lstrip('/')])

        try: resp_code = requests.get(request_url).status_code
        except: continue

        if resp_code in [200, 301, 403]:
            return {domain: request_url}

    return {domain: False}