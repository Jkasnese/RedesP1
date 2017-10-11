﻿import socket
import time
import fcntl
import struct
from util_protocolo_com import *
from util_com import *
from threading import Thread
from medico_medico import *

lista_risco = [] # Armazena o CPF de todos os pacientes que estão em risco. Cada index um paciente. Dentro de cada paciente: [0] = CPF, [1] = BPM, [2] = Pressao, [3] = Movimento
paciente_monitorado = [] # [0] = CPF, [1] = BPM, [2] = Pressao, [3] = Movimento, [4] = Monitoramento ativo

""" Cria novo medico, cadastra no servidor, solicita permanentemente lista de risco.
    Retorna medico e socket da conexão do médico
"""
def novo_medico(nome, crm, senha, ip_servidor, porta_servidor):
    # Cria novo objeto médico
    novo_medico = Medico(nome, crm)

    # Cadastrar o socket de comunicação do médico com o servidor
    bocal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bocal.connect((ip_servidor, porta_servidor))

    # Cadastrar médico no servidor
    solicitar_cadastro_medico(novo_medico, senha, bocal)

    # Criar nova Thread pra pedir lista de risco permanentemente p/ servidor
    thread_atualiza_lista = Thread(target = solicitar_lista_risco, args=(novo_medico.crm, bocal, lista_risco), daemon=True)
    thread_atualiza_lista.start()

    return novo_medico, bocal

# Envia p/ servidor: 2CRM|NOME|SENHA
def solicitar_cadastro_medico(medico, senha, bocal):
    mensagem = "2" + medico.crm + caracter_separador + medico.nome + caracter_separador + senha
    controle_envio_resposta(mensagem, bocal)
    return

def autenticar_medico(crm, senha, bocal):
    mensagem = "3" + crm + senha
    controle_envio_resposta(mensagem, bocal)
    return

""" Retorna lista de pacientes em risco"""
def solicitar_lista_risco(crm, bocal, lista_risco):
    print("Atualizando lista de risco")
    while True:        
        mensagem = "4" + crm
        time.sleep(1)
        resposta = controle_envio_resposta(mensagem, bocal) 
        lista_risco = resposta[1:].split(separador_pacientes) 
    print("Parou de atualizar lista de risco")

def buscar_paciente(crm, cpf, bocal):
    mensagem = "5" + crm + caracter_separador + cpf
    resposta = controle_envio_resposta(mensagem, bocal)
    return resposta     #CPF|BPM|PRESSAO|MOVIMENTO

# Envia: CRM|BOCAL|PORTA_UDP|IP_CLIENTE
def selecionar_paciente_monitorado(crm, cpf, bocal, porta_udp):
    # Configura monitorado [4] como verdadeiro
    paciente_monitorado[4] = True

    # Abre socket UDP pra ouvir os dados do paciente monitorado
    socket_UDP = abrirSocketUDP(porta_udp)
    threadOuvirUDP = Thread(target = self.receber_paciente_monitorado, args=(socket_UDP,))
    threadOuvirUDP.start()

    # Consegue o IP do cliente
    ifname = 'eth0'
    ip_cliente =    socket.inet_ntoa(fcntl.ioctl(
                        socket_UDP.fileno(),
                        0x8915,  # SIOCGIFADDR
                        struct.pack('256s', ifname[:15])
                    )[20:24])
    
    # Constrói mensagem e envia
    mensagem = "6" + crm + caracter_separador + cpf + caracter_separador + porta_udp + caracter_separador + ip_cliente
    controle_envio_resposta(mensagem, bocal)
    return

def excluir_paciente_monitorado(crm, bocal):
    mensagem = "7" + crm
    resposta = controle_envio_resposta(mensagem, bocal)
    paciente_monitorado[4] = False
    return resposta
    

def receber_paciente_monitorado(bocal):
    while paciente_monitorado[4] != False:
        mensagem, addr = ouvir_socket(bocal)
        print("Recebido: ", mensagem, end="|")       
        paciente_monitorado = mensagem  #CPF|BPM|PRESSAO|MOVIMENTO
    
def controle_envio_resposta(mensagem, bocal):
    resposta = "1"
    tentativa = 0
    while (resposta[0] != "0" and tentativa < 3):
        # Envia msg e retorna a resposta
        enviar_TCP(mensagem, bocal)
        resposta = ouvirTCP(bocal)
        print ("Enviado: ", mensagem)
        print("Resposta: ", resposta)
        time.sleep(1)
        tentativa += 1
    return resposta



""" Atualiza lista de pacientes em risco
def atualizar_lista_risco(lista_risco, crm, bocal):
    nova_lista_risco = solicitar_lista_risco(crm, bocal)
    # Diz que todos da lista velha estão desatualizados
    for j in lista_risco:
        j[1] = False    
    # Itera em cada um da nova lista
    for i in nova_lista_risco:
        dados = i.split(caracter_separador) # Separa os dados
        dicionario_risco[dados[0]] = [dados[1], dados[2], dados[3]] #Adiciona os novos dados no dicionário
        for j in lista_risco:
            if (dados[0] == j[0]): # Se os CPFs forem iguais, paciente foi atualizado
                j[1] = True
        for k in lista_risco:
            if (j[1] == False):
                lista_risco"""

# TESTE

#porta = int(input("Digite a porta TCP: "))
#medico, bocal = novo_medico("Joao", "123", "admin", "127.0.0.1", porta)
#time.sleep(1)
#buscar_paciente("123", "Buba", bocal)
#time.sleep(15)
#buscar_paciente("123", "Buba", bocal)

