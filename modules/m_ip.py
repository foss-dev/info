import requests as r
import json

def remote_url():
    resp = r.get("http://ip-api.com/json")

    return json.loads(resp.text)

def get_ip(request):
    data = {}

    remote = remote_url()
    data["local"] = request.remote_addr
    data["remote"] = remote

    return data
