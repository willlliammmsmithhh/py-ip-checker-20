import socket
def validate(addr):
    for fam in (socket.AF_INET, socket.AF_INET6):