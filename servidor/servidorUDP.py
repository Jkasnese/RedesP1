import socket

UDP_IP = "127.0.0.1"

def abrirSocketUDP():
    UDP_PORT = int(input("Digite a porta da comunicacao UDP"))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    return sock

def levantarServidorUDP(socket):
    while True:
        data, addr = socket.recvfrom(1024) # buffer size is 1024 bytes
        print ("Mensagem recebidabbbb:", data)


# Testando
#socket = abrirSocketUDP()
#levantarServidorUDP(socket)
