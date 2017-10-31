#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
from util_protocolo_com import *
from util_com import *
from threading import Thread

#Achar jeito melhor pra importar
from sensor_sensor import *

""" Classe correspondente ao controller de sensores, pra ser usada na interface que simula um sensor
    Responsavel por comunicar o model de sensor com a interface
"""


#Cria um novo sensor e atribui valores aleatorios a ele
def selecionaValores(sensor):
    #Imprimindo os sensores
    # Incluir função pra enviar ID depois print(sensor.id)
    mensagem = str(sensor.identificador) + caracter_separador
    mensagem += str(sensor.bpm) + caracter_separador
    mensagem += str(sensor.pressao.value) + caracter_separador
    mensagem += str(sensor.movimento) + caracter_separador
    mensagem += str(sensor.x) + caracter_separador
    mensagem += str(sensor.y) + caracter_separador
    return mensagem


def enviarValores(sensor, ip_servidor):
    """ Envia valores aleatorios continuamente ate o usuario modificar o valor.
    A partir dai, envia os valores definidos pelo usuario"""

    # Comando p/ atualizar dados do sensor
    mensagem = "1"
    contador = 0
    while(True):
        time.sleep(1)
        contador += 1
        if (sensor.modificado == False):
            sensor.gerarValores()
        mensagem = "1" + selecionaValores(sensor)
        enviarUDP(mensagem, ip_servidor) # Adicionar TRY/CATCH aqui PENDENTE
        print("Enviado: ", mensagem)
        # Mecanismo p/ realocar sensor PENDENTE
        #if (contador%60 == 0): # A cada minuto:
            #enviarUDP("8" + caracter_separador + sensor.x + caracter_separador + sensor.y)

def cadastrarSensor(sensor, bocal):
    # Define mensagem de cadastro
    mensagem = "0" + sensor.cpf + caracter_separador + sensor.identificador + caracter_separador + str(sensor.x) + caracter_separador + str(sensor.y)
    resposta = "-1"
    # Tratar melhor caso conexão falhe após X tentativas ou X tempos.
    while (resposta == "-1"):
        # Envia msg e retorna a resposta
        resposta = enviar_cadastro_TCP(mensagem,bocal)
        print ("Enviado: ", mensagem)
        print("Resposta: ", resposta)
    return resposta

def novoSensor(cpf, ip_servidor, tcp_porta):
    # Criar novo sensor
    novoSensor = Sensor(cpf)
    novoSensor.gerarValores()

    # Cadastrar sensor no servidor. Cria socket e envia cadastro por meio dele até receber confirmação do cadastro
    bocal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bocal.connect((ip_servidor, tcp_porta))
    ip_servidor = cadastrarSensor(novoSensor, bocal)
    print("Sensor cadastrado!")
    ## Fechar porta TCP PENDENTE

    # Depois de cadastrado, começar a enviar valores
    threadEnviaValores = Thread(target = enviarValores, args = (novoSensor, ip_servidor), daemon=True)
    threadEnviaValores.start()
    return novoSensor



###Teste

#Criando Sensor
#novoSensor = novoSensor()
#print("Novo sensor BPM: " + novoSensor.bpm)
