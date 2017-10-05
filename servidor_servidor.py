import socket
from util_comUDP import *
# Achar jeito melhro pra importar
from sensor_sensor import *
from threading import Thread
from util_protocoloCom import *

#import comunicacaoTCP

class Servidor:

    def __init__(self):
        self.sensores = {}
        self.id_sensores = []
        self.medicos = {}
        self.endereco_medicos = []
        
        self.socketUDP = abrirSocketUDP(int(input("Digite a porta da comunicacao UDP: ")))
        threadOuvir = Thread(target = self.ouvirSocketUDP, args = (self.socketUDP,))
        threadOuvir.start()

    def ouvirSocketUDP(self, socket):
        while True:
            mensagem, endereço = ouvirUDP(self.socketUDP)
            print("Recebido: ", mensagem, end="|")        
            print("De: ", endereço)
            porta = endereço[1]
            endereço = str(endereço[0])

            print(" - - - - Executando comando: " + mensagem[0] + " - - - - ")
            if ('0' == mensagem[0]):
                self.cadastrarSensor(mensagem[1:], endereço, porta)
            elif ('1' == mensagem[0]):
                self.atualizarSensor(mensagem[1:])
            elif ('2' == mensagem[0]):
                self.cadastrarMedico(mensagem[1:])
            elif ('3' == mensagem[0]):
                self.atualizarMedico(mensagem[1:])
            else:
                self.repitaMensagem(endereço, porta)      

    def cadastrarSensor(self, mensagem, endereço, porta):
        # Separa o CPF do ID        
        cpf = mensagem.split(caracter_separador)
        identificador = cpf[1]
        cpf = cpf[0]

        # Cadastra novo sensor
        novoSensor = Sensor(cpf, identificador)
        self.sensores[identificador] = novoSensor
        print("Cadastrado sensor: " + self.sensores[identificador].cpf)

        # Adiciona ID do sensor na lista de sensores
        self.id_sensores.append(identificador)
    
        # Adiciona endereço do sensor na lista de endereços
        endereço_completo = str(endereço) + ";" + str(porta)
        #self.endereco_sensores.append(endereço_completo)
        #print("No endereço: ", endereço_completo)
        
        # Resposta ao cadastro
        resposta = '0'
        enviarUDP(resposta, endereço, porta)
        print("Enviado: " + resposta + " p/: " + endereço_completo)
        
    def atualizarSensor(self, mensagem):
        # Atualiza os dados do sensor correspondente ao endereço recebido
        mensagem = mensagem.split(caracter_separador)
        identificador = mensagem[0]
        self.sensores[identificador].bpm = mensagem[1]
        self.sensores[identificador].pressao = int(mensagem[2])
        self.sensores[identificador].movimento = mensagem[3]
        print("Atualizando sensor: " + identificador)
        print("BPM: " + self.sensores[identificador].bpm + " Pressao: " + str(self.sensores[identificador].pressao) + " Movimento: " + str(self.sensores[identificador].movimento))
        
    def cadastrarMedico(self, mensagem):
        print("Cadatrar medico")
                
    def atualizarMedico(self, mensagem):
        print("Atualizar medico")

    def repitaMensagem(self, mensagem):
        print("Repita mensagem")
            
            
            
            
servidor = Servidor()
