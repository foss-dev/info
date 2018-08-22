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
    types_dict = {
        'hacked_emails'    : lambda x: hacked_emails(x),
        'have_i_been_pwned': lambda x: have_i_been_pwned(x),
        'password'         : lambda x: {'password_count': password(x)}
    }

    return types_dict.get(types, lambda *args: None)(keyword)