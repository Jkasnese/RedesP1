import socket
from servidorUDP import *

#Achar jeito melhor pra importar
import sys
sys.path.insert(0, '/home/guiga/Desktop/Guiga/UEFEY/5_semestre_Redes/MI/P1/sensor')
from sensor import *

#import comunicacaoTCP

class Servidor:

    def __init__(self):
        self.sensores = []
        self.medicos = []
        socket = abrirSocketUDP()
        self.ouvirSocket(socket)

    def ouvirSocket(self, socket):
        while True:
            data, addr = socket.recvfrom(1024) # buffer size is 1024 bytes
            print ("Mensagem recebida:", data, "De: ", addr)
            
            
            
            
servidor = Servidor()
