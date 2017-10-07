import socket
from util_comUDP import *
# Achar jeito melhro pra importar
from sensor_sensor import *
from threading import Thread
from util_protocoloCom import *
from queue import Queue

#import comunicacaoTCP

class Servidor:

    def __init__(self):
        # Dados
        self.sensores = {}
        self.id_sensores = []
        self.medicos = {}
        self.endereco_medicos = []

        # UDP
        self.socketUDP = abrirSocketUDP(int(input("Digite a porta da comunicacao UDP: ")))
        threadOuvirUDP = Thread(target = self.receber_mensagem, args=(self.socketUDP,))
        threadOuvirUDP.start()

        # TCP
        # Abrir bocal e ouvir até receber nova conexão
        self.socketTCP = abrirSocketTCP(int(input("Digite a porta da comunicao TCP: ")))
        self.socketTCP.listen(10)
        # Ao receber nova conexão, aceita a conexão e coloca o socket desta na fila lista_conexoes
        lista_conexoes = Queue()
        thread_abrir_conexoes = Thread(target = aceitar_conexoes, args=(self.socketTCP, lista_conexoes))
        thread_abrir_conexoes.start()
        
        # Socket é retirado da fila e passado para função de ouvir, p/ que servidor registre as mensagens do socket.
        # Recebe tupla contendo socket e endereço
        bocal = lista_conexoes.get()
        print(bocal)
        endereço = bocal[1]
        bocal = bocal[0]
        print("Antes de chamar receber_mensagem: " + str(endereço))
        thread_ouvir_TCP = Thread(target = self.receber_mensagem, args=(bocal, endereço))
        thread_ouvir_TCP.start()

    def receber_mensagem(self, bocal, endereço=('','')):
        print("Dentro de receber_msg: " + str(endereço))
        while True:
            mensagem, addr = ouvir_socket(bocal)
            print("Recebido: ", mensagem, end="|")       
            # Caso seja UDP ele recebeu msg,endereço. Caso seja TCP recebeu só msg. Diferenciar:
            if (None == addr):
                print("De: ", endereço)
                porta = endereço[1]
                endIP = str(endereço[0])
            else:
                print("De: ", addr)
                porta = addr[1]
                endIP = str(addr[0])

            print(" - - - - Executando comando: " + mensagem[0] + " - - - - ")
            if ('0' == mensagem[0]):
                self.cadastrarSensor(mensagem[1:], endIP, porta, bocal)
            elif ('1' == mensagem[0]):
                self.atualizarSensor(mensagem[1:])
            elif ('2' == mensagem[0]):
                self.cadastrarMedico(mensagem[1:])
            elif ('3' == mensagem[0]):
                self.atualizarMedico(mensagem[1:])
            else:
                self.repitaMensagem(endIP, porta)

    def cadastrarSensor(self, mensagem, endereço, porta, bocal):
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
        enviarTCP(resposta, bocal)
        print("Enviado: " + resposta + " p/: " + endereço_completo)
        
    def atualizarSensor(self, mensagem):
        # Atualiza os dados do sensor correspondente ao endereço recebido
        mensagem = mensagem.split(caracter_separador)
        identificador = mensagem[0]
        self.sensores[identificador].bpm = mensagem[1]
        self.sensores[identificador].pressao = int(mensagem[2])
        self.sensores[identificador].movimento = bool("True" == mensagem[3])
        print("Atualizando sensor: " + identificador)
        print("BPM: " + self.sensores[identificador].bpm + " Pressao: " + str(self.sensores[identificador].pressao) + " Movimento: " + str(self.sensores[identificador].movimento))
        
    def cadastrarMedico(self, mensagem):
        print("Cadatrar medico")
                
    def atualizarMedico(self, mensagem):
        print("Atualizar medico")

    def repitaMensagem(self, mensagem):
        print("Repita mensagem")
            
            
            
            
servidor = Servidor()
