import socket
import time
from util_protocoloCom import *
from util_comUDP import *
from threading import Thread
from medico_medico import *

lista_risco = [] # Armazena o CPF de todos os pacientes que estão em risco. Cada index um paciente. Dentro de cada paciente: [0] = CPF, [1] = BPM, [2] = Pressao, [3] = Movimento
paciente_monitorado = [] # [0] = CPF, [1] = BPM, [2] = Pressao, [3] = Movimento

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
    thread_atualiza_lista = Thread(target = solicitar_lista_risco, args=(novo_medico.crm, bocal, lista_risco))
    thread_atualiza_lista.start()

    return medico, bocal

def solicitar_cadastro_medico(medico, senha, bocal):
    mensagem = "2" + medico.crm + caracter_separador + medico.nome
    controle_envio_resposta(mensagem, bocal)
    return

def autenticar_medico(crm, senha, bocal):
    mensagem = "3" + crm, senha, bocal
    controle_envio_resposta(mensagem, bocal)
    return

""" Retorna lista de pacientes em risco"""
def solicitar_lista_risco(crm, bocal, lista_risco):
    mensagem = "4" + medico.crm
    resposta = controle_envio_resposta(mensagem, bocal) 
    lista_risco = resposta[1:].split(separador_pacientes) 
    return     

def buscar_paciente(crm, cpf, bocal):
    mensagem = "5" + crm + caracter_separador + bocal
    resposta = controle_envio_resposta(mensagem, bocal)
    return resposta     #CPF|BPM|PRESSAO|MOVIMENTO

def selecionar_paciente_monitorado(crm, cpf, bocal, porta_udp):
    mensagem = "6" + crm + caracter_separador + bocal
    socket_UDP = abrirSocketUDP(porta_udp)
    threadOuvirUDP = Thread(target = self.receber_paciente_monitorado, args=(socket_UDP,))
    threadOuvirUDP.start()
    controle_envio_resposta(mensagem, bocal)
    return

def receber_paciente_monitorado(bocal):
    while True:
        mensagem, addr = ouvir_socket(bocal)
        print("Recebido: ", mensagem, end="|")       
        paciente_monitorado = mensagem  #CPF|BPM|PRESSAO|MOVIMENTO
    
def controle_envio_resposta(mensagem, bocal):
    resposta = "1"
    while (resposta[0] != "0"):
        # Envia msg e retorna a resposta
        enviar_TCP(mensagem, bocal)
        resposta = ouvirTCP(bocal)
        print ("Enviado: ", mensagem)
        print("Resposta: ", resposta)
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


    

    
    
