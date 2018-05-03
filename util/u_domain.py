import re

def domain_resolve(domain):
    domain = re.sub("(http|https)://", "", domain).rstrip('/')

    return domain