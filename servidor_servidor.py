import time
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
        self.sensores = {} # Recebe tudo string
        self.id_sensores = []
        self.medicos = {} # Index = CRM. ELementos = [nome, senha, thread_monitoramento]
        self.crm_medicos = []
        self.threads_ouvintes_TCP = {}

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
        thread_cria_bocal = Thread(target = self.recebe_bocal, args=(lista_conexoes,))
        thread_cria_bocal.start()

    def recebe_bocal(self, lista_conexoes):
        while True:
            bocal = lista_conexoes.get()
            endereço = bocal[1]
            bocal = bocal[0]
            thread_ouvir_TCP = Thread(target = self.receber_mensagem, args=(bocal, endereço))
            self.threads_ouvintes_TCP[bocal] = thread_ouvir_TCP
            thread_ouvir_TCP.start()            

    def receber_mensagem(self, bocal, endereço=('','')):
        mensagem = '0'
        while (mensagem != ''):
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

            # Se recebeu '' é porque o outro host fechou a conexão
            if (mensagem == ''):
                break;
            else:
                print(" - - - - Executando comando: " + mensagem[0] + " - - - - ")
                if ('0' == mensagem[0]):
                    self.cadastrarSensor(mensagem[1:], bocal)
                elif ('1' == mensagem[0]):
                    self.atualizarSensor(mensagem[1:])
                elif ('2' == mensagem[0]):
                    self.cadastrar_medico(mensagem[1:], bocal)
                elif ('3' == mensagem[0]):
                    self.autenticar_medico(mensagem[1:], bocal)
                elif ('4' == mensagem[0]):
                    self.enviar_lista_risco(mensagem[1:], bocal)
                elif ('5' == mensagem[0]):
                    self.buscar_paciente(mensagem[1:], bocal)
                elif ('6' == mensagem[0]):
                    self.monitorar_paciente(mensagem[1:])
                else:
                    self.repita_mensagem(bocal)
        # Caso saia do while, não está mais escutando. Posso fechar o bocal.
        bocal.close()

    def cadastrarSensor(self, mensagem, bocal):
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
#        endereço_completo = str(endereço) + ";" + str(porta)
        #self.endereco_sensores.append(endereço_completo)
        #print("No endereço: ", endereço_completo)
        
        # Resposta ao cadastro
        resposta = '0'
        # Envia resposta final do servidor ao sensor, antes de fechar conexão
        enviar_TCP(resposta, bocal)
        print("Enviado: " + resposta)
        
    def atualizarSensor(self, mensagem):
        # Atualiza os dados do sensor correspondente ao endereço recebido
        mensagem = mensagem.split(caracter_separador)
        identificador = mensagem[0]
        self.sensores[identificador].bpm = int(mensagem[1])
        self.sensores[identificador].pressao = int(mensagem[2])
        self.sensores[identificador].movimento = bool("True" == mensagem[3])
        print("Atualizando sensor: " + identificador)
        print("BPM: " + str(self.sensores[identificador].bpm) + " Pressao: " + str(self.sensores[identificador].pressao) + " Movimento: " + str(self.sensores[identificador].movimento))
    
    """Recebe mensagem com formato: CRM|NOME|SENHA, de acordo com o protocolo, e cadastra o médico no dicionário de médicos"""
    def cadastrar_medico(self, mensagem, bocal):
        # Cadastra médico
        mensagem = mensagem.split(caracter_separador)
        self.medicos[mensagem[0]] = [mensagem[1], mensagem[2]]
             # Coloca crm na lista de crms
        self.crm_medicos.append(mensagem[1])

        if (self.medicos[mensagem[0]] != None):
            print("Medico cadastrado! " + self.medicos[mensagem[0]][1] )
            # Responde ao cadastro
            resposta = '0'
        else:
            resposta = '1'
        # Envia resposta do servidor
        enviar_TCP(resposta, bocal)
        print("Enviado: " + resposta)
        return        

    """ Envia lista no formato: CPF|BPM|PRESSAO|MOVIMENTO, de acordo com protocolo"""
    def enviar_lista_risco(self, mensagem, bocal):
        resposta = '0'
        # Itera na lista de sensores e coloca sensores em risco na lista
        if not self.id_sensores:
            print("Nao ha sensores cadastrados no servidor!")
            enviar_TCP('1', bocal)
            return
        for i in self.id_sensores:
            bpm = self.sensores[i].bpm
            movimento = self.sensores[i].movimento
            if ( (bpm > 100 and movimento == False) or ( bpm < 40 and movimento == False) ):
                resposta += self.sensores[i].cpf + caracter_separador
                resposta += str(bpm) + caracter_separador
                resposta += str(self.sensores[i].pressao) + caracter_separador
                resposta += str(movimento) + separador_pacientes
        enviar_TCP(resposta, bocal)
        print("")        
        print("Enviada lista de risco p/ medico: " + mensagem)
        print(resposta)
        print("")
        return


    """ Recebe CRM|CPF
        Retorna: #CPF|BPM|PRESSAO|MOVIMENTO"""
    def buscar_paciente(self, mensagem, bocal):
        mensagem = mensagem.split(caracter_separador) # 0 crm 1 é cpf
        for i in self.id_sensores:
            if (i == mensagem[1]):
                resposta = self.sensores[mensagem[1]].cpf + caracter_separador
                resposta += str(self.sensores[mensagem[1]].bpm) + caracter_separador
                resposta += str(self.sensores[mensagem[1]].pressao) + caracter_separador
                resposta += str(self.sensores[mensagem[1]].movimento)
                print("Enviado paciente: " + mensagem[1] + " para medico: " + mensagem[0])
                enviar_TCP(resposta, bocal)
                return resposta
        # Caso não esteja na lista
        enviar_TCP('1', bocal)    
        return '1'


    # Recebe: CRM|CPF|PORTA_UDP|IP_CLIENTE
    # Envia: #CPF|BPM|PRESSAO|MOVIMENTO
    def monitorar_paciente(self, mensagem):
        # Recebe mensagem e inicia thread de enviar
        mensagem = mensagem.split(caracter_separador)
        self.medicos[mensagem[0]][4] = True
        thread_enviar_monitorado = Thread(target=enviar_monitorado, args=(mensagem[0], mensagem[1], mensagem[2], mensagem[3]))
        thread_enviar_monitorado.start()
        print("Enviando paciente " + mensagem[1] + " para: " + mensagem[0])
        return

    def enviar_monitorado(self, crm, cpf, porta_udp, ip_cliente):
        while (self.medicos[crm][4] == True):
            mensagem = cpf + caracter_separador
            mensagem += str(self.sensores[cpf].bpm) + caracter_separador
            mensagem += str(self.sensores[cpf].pressao) + caracter_separador
            mensagem += str(self.sensores[cpf].movimento)
            enviarUDP(mensagem, porta_udp, ip_cliente)

    def parar_monitoramento(self, crm, bocal):
        self.medicos[crm][4] = False
        enviar_TCP('0', bocal)
        return

    def repita_mensagem(self, bocal):
        enviar_TCP("Repita mensagem!", bocal)        
        print("Repita mensagem!")
            
            
            
            
servidor = Servidor()
