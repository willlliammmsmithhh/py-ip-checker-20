import socket
def validate(addr):
    for fam in (socket.AF_INET, socket.AF_INET6):
        try:
            socket.inet_pton(fam, addr)
            return True
        except socket.error:
            pass
    return False