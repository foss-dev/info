import os, json
import requests

json_file = os.path.join(os.path.dirname(__file__), '..', 'extra', 'mybb_plugins.json')
json_data = json.loads(open(json_file, 'r').read())

def plugin_scanner(domain):
    results = []

    for info in json_data:
        url = 'http://' + '/'.join([domain, 'inc', 'plugins', info['plugin_file']])

        try: resp_code = requests.get(url).status_code
        except: continue

        if resp_code == 200:
            results.append(info)

    return results