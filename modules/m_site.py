import requests as r
from bs4 import BeautifulSoup
import re

def info(domain):
    results = {}
    newDomain = "https://{}".format(domain)
    
    resp = r.get(newDomain)

    site = BeautifulSoup(resp.text, 'html.parser')

    site_scripts = []
    site_css = []

    scripts = site.find_all("script", {"src": True})
    css_list = site.find_all("link", {"href": True, "rel":"stylesheet", "type":"text/css"})
    
    for script in scripts:
        site_scripts.append(script["src"])
    
    for css in css_list:
        site_css.append(css["href"])

    results['status_code'] = resp.status_code
    results['title'] = site.title.string
    results['scripts'] = site_scripts
    results['css_list'] = site_css

    return results