import netaddr

def scan(ip, mini, maxi):
    ip_start = ip.split('.')
    ip_block = ".".join(ip_start[:3]) + ".{}/{}".format(mini, maxi)
    data = []

    for i in range(0, 255):
        ip_address = ".".join(ip_start[:3]) + "." + str(i)
        if ip_address in netaddr.IPNetwork(ip_block):
            data.append({
                "ip": ip_address,
                "status": True
            })
        else:
            data.append({
                "ip": ip_address,
                "status": False
            })
        
    return data


