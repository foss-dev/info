import socket

def check_port(domain, port, timeout=0.5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    result = sock.connect_ex((domain, int(port)))
    return {'status': not result} # 0: True, 1: False