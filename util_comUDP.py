import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

def enviarUDP(UDP_IP, MESSAGE):
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(str.encode(MESSAGE), (UDP_IP, UDP_PORT))

def abrirSocketUDP(UDP_PORT=5005):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    return sock

def ouvirUDP(socket):
    while True:
        data, addr = socket.recvfrom(1024) # buffer size is 1024 bytes
        return bytes.decode(data), addr

