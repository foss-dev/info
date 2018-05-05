import requests as r
import re
import math

from bs4 import BeautifulSoup


base_url = "https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query={}&search_type=all"

def cve_result(keyword):

    cve_list = []

    resp = r.get(base_url.format(keyword))

    site = BeautifulSoup(resp.text, 'html.parser')

    cve_title = site.select(".table > tbody > tr > th > strong > a")
    cve_desc = site.select(".table > tbody > tr > td > p")
    cve_publish = site.select(".table > tbody > tr > td:nth-of-type(1) > span")
    cve_severity = site.select(".table > tbody > tr > td:nth-of-type(2) > span")
    total_data = site.select("strong[data-testid='vuln-matching-records-count']")[0].text
    total_page = math.ceil(float(total_data.replace(',', '')) / 20)

    cve_list.append({
        "total": total_data,
        "page_count": total_page
    })

    for i in range(len(cve_title)):
        cve_list.append({
            "url": cve_title[i].get('href'),
            "title": cve_title[i].text,
            "description": cve_desc[i].text,
            "severity": cve_severity[i].text,
            "publish": cve_publish[i].text
        })

    return cve_list