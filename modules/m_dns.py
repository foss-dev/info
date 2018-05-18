from dns import resolver

"""DNS Record Types"""
types = [
    'A',
    'NS',
    'CNAME',
    'SOA',
    'PTR',
    'HINFO',
    'MINFO',
    'MX',
    'TXT',
    'AAAA',
    'LOC',
    'NXT',
    'SRV',
    'APL',
    'DS',
    'DNSKEY',
    'TLSA',
    'SPF',
]

def dns_records(domain):
    records = {}

    for t in types:
        try:
            response = resolver.query(domain, t)
            for data in response:
                records[t] = data.to_text()
        except:
            records[t] = "null"

    return records
