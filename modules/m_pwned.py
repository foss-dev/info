import requests as r
import json

def have_i_been_pwned(keyword):
    url = "https://haveibeenpwned.com/api/v2/unifiedsearch/{}".format(keyword)

    resp = r.get(url)

    return json.loads(resp.text)

def hacked_emails(keyword):
    url = "https://hacked-emails.com/api?q={}".format(keyword)

    resp = r.get(url)

    return json.loads(resp.text)

def password(keyword):
    url = "https://api.pwnedpasswords.com/pwnedpassword/{}".format(keyword)

    resp = r.get(url)

    return resp.text

def pwned(types, keyword):
    data = {}

    if types == "have_i_been_pwned":
        data = have_i_been_pwned(keyword)
    elif types == "hacked_emails":
        data = hacked_emails(keyword)
    elif types == "password":
        data["password_count"] = password(keyword)
    
    return data