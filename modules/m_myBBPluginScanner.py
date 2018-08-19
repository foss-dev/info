from requests import get
from os import getcwd, sep
from json import load

jsonFile = getcwd()+sep+"extra"+sep+"mybbPlugins.json"

with open(jsonFile) as dataFile:
    data = load(dataFile)

def pluginScanner(domain):
    results = []

    for info in data:
        try:
            url = "http://{}/inc/plugins/{}".format(domain, info["pluginFile"])
            request = get(url).status_code

            if request == 200:
                payload = {"bbPluginName": info["pluginName"]}
                payload["bugs"] = []
                for bug in info["bugs"]:
                    test = {"title": bug["title"], "exdb": bug["exdb"]}
                    payload["bugs"].append(test)
                results.append(payload)
        except:
            pass

    return results
