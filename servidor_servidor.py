import socket
from util_comUDP import *
# Achar jeito melhro pra importar
from sensor_sensor import *
from threading import Thread

#import comunicacaoTCP

class Servidor:

    def __init__(self):
        self.sensores = {}
        self.endereco_sensores = []
        self.medicos = {}
        self.endereco_medicos = []
        
        self.socketUDP = abrirSocketUDP(int(input("Digite a porta da comunicacao UDP: ")))
        threadOuvir = Thread(target = self.ouvirSocketUDP, args = (self.socketUDP,))
        threadOuvir.start()

    def ouvirSocketUDP(self, socket):
        mensagem, endereço = ouvirUDP(self.socketUDP)
        endereço = str(endereço)
        print("Recebido: ", mensagem)
        print(mensagem[0])
        if ('0' == mensagem[0]):
            self.cadastrarSensor(mensagem, endereço)
        elif ('1' == mensagem[0]):
            self.atualizarSensor(mensagem)
        elif ('2' == mensagem[0]):
            self.cadastrarMedico(mensagem)
        elif ('3' == mensagem[0]):
            self.atualizarMedico(mensagem)
        else:
            self.repitaMensagem(endereço)      
            

    def cadastrarSensor(self, mensagem, endereço):
        # Adiciona o sensor no dicionário de sensores
        novoSensor = Sensor(mensagem[1:])
        self.sensores[endereço] = novoSensor
        print("Cadastrado sensor: " + self.sensores[endereço].cpf)

        # Adiciona endereço do sensor na lista de endereços
        self.endereco_sensores.append(endereço)
        print("No endereço: " + endereço)
        
        # Resposta ao cadastro
        print(type(endereço))
        resposta = '0'
        enviarUDP(endereço, resposta)
        
        

    def atualizarSensor(self, mensagem):
        print("Atualizar sensor")
        
    def cadastrarMedico(self, mensagem):
        print("Cadatrar medico")
            
    def atualizarMedico(self, mensagem):
        print("Atualizar medico")

    def repitaMensagem(self, mensagem):
        print("Repita mensagem")
            
            
            
            
servidor = Servidor()
