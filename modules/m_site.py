import requests as r
from bs4 import BeautifulSoup
import re

cms_list = [
    "WordPress", "Joomla", "Ghost", "Drupal",
    "Textpattern","Hugo", "Jekyll", "SilverStripe",
    "concrete5", "Nikola", "DokuWiki", "Pixie",
    "ProcessWire", "Serendipity", "blogger", "Tiki Wiki",
    "b2evolution", "MediaWiki", "OctoberCMS", "vBulletin",
    "Discourse"
]

def cms_parser(parsed):
    cms_name = ""
    for cms in cms_list:
        if parsed["generator"] is not None:
            if cms in parsed["generator"]:
                cms_name = cms
                break
            else:
                cms_name = parsed["generator"]
    
    return cms_name.title()

def meta_parser(meta_list):
    meta_obj = {
        "generator": None
    }
    
    try:
        meta_obj["charset"] = meta_list[0].get('charset')
    except:
        meta_obj["charset"] = None

    for meta in meta_list:
        if meta.get("name", None) is not None:
            meta_obj[meta.get("name", None)] = meta.get("content", None)
        elif meta.get("property", None) is not None:
            meta_obj[meta.get("property", None)] = meta.get("content", None)

    return meta_obj

def link_parser(link_list):
    link_obj = {
        "profile": [],
        "stylesheet": [],
        "pingback": [],
        "canonical": [],
        "dns-prefetch": [],
        "alternate": [],
        "icon": []
    }

    for link in link_list:
        try:
            link_obj[link.get("rel")[0]].append(link.get("href", None))
        except:
            link_obj[link.get("rel")[0]] = link.get("href", None)
    
    return link_obj


def info(domain):
    results = {}
    newDomain = "https://{}".format(domain)
    
    resp = r.get(newDomain)

    site = BeautifulSoup(resp.text, 'html.parser')

    site_scripts = []
    site_css = []
    meta_tags = []
    links = []

    scripts = site.find_all("script", {"src": True})
    css_list = site.find_all("link", {"href": True, "rel":"stylesheet", "type":"text/css"})
    meta_list = site.find_all("meta")
    link_list = site.find_all("link")

    for script in scripts:
        site_scripts.append(script["src"])
    
    for css in css_list:
        site_css.append(css["href"])
    
    meta_parsed = meta_parser(meta_list)
    link_parsed = link_parser(link_list)
    cms = cms_parser(meta_parsed)
    
    meta_tags.append(meta_parsed)
    links.append(link_parsed)

    results['status_code'] = resp.status_code
    results['title'] = site.title.string
    results['scripts'] = site_scripts
    results['css_list'] = site_css
    results['meta'] = meta_tags
    results["links"] = links
    results["cms"] = cms

    return results