import socket

def check_port(domain, port):
    response = {
        "status": False
    }

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((domain, int(port)))

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((domain, int(port)))

        if result == 0:
            response["status"] = True
    except:
        response["status"] = False
    
    return response

