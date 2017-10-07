#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
from util_protocoloCom import *
from util_comUDP import *
from threading import Thread

#Achar jeito melhor pra importar
from sensor_sensor import *

""" Classe correspondente ao controller de sensores, pra ser usada na interface que simula um sensor
    Responsavel por comunicar o model de sensor com a interface
"""

UDP_IP = "127.0.0.1"

#Cria um novo sensor e atribui valores aleatorios a ele
def selecionaValores(sensor):
    #Imprimindo os sensores
    # Incluir função pra enviar ID depois print(sensor.id)
    mensagem = str(sensor.identificador) + caracter_separador
    mensagem += str(sensor.bpm) + caracter_separador
    mensagem += str(sensor.pressao.value) + caracter_separador
    mensagem += str(sensor.movimento) + caracter_separador
    return mensagem


def enviarValores(sensor):
    """ Envia valores aleatorios continuamente ate o usuario modificar o valor.
    A partir dai, envia os valores definidos pelo usuario"""

    # Comando p/ atualizar dados do sensor
    mensagem = "1"    
    while(True):
        time.sleep(1)
        if (sensor.modificado == False):
            sensor.gerarValores()
        mensagem = "1" + selecionaValores(sensor)
        enviarUDP(mensagem, UDP_IP)
        print("Enviado: ", mensagem)

def cadastrarSensor(sensor):
    # Define mensagem de cadastro
    mensagem = "0" + sensor.cpf + ";" + sensor.identificador
    resposta = "1"
    while (resposta != "0"):
        # Envia msg e retorna o socket de envio
        bocal = enviarUDP(mensagem, UDP_IP)
        print ("Enviado: ", mensagem)
        # Aguarda resposta neste bocal
        resposta, endereço = ouvir_socket(bocal)
        print("Resposta: ", resposta)
        print("De: " + endereço[0] + ";" + str(endereço[1]))

def novoSensor():
    cpf = input("Digite o CPF do sensor: ")
    novoSensor = Sensor(cpf)
    novoSensor.gerarValores()
    # Cadastrar sensor no servidor
    cadastrarSensor(novoSensor)
    print("Sensor cadastrado!")
    # Depois de cadastrado, começar a enviar valores
    threadEnviaValores = Thread(target = enviarValores, args = (novoSensor,))
    threadEnviaValores.daemon = True
    threadEnviaValores.start()
    return novoSensor



###Teste

#Criando Sensor
#novoSensor = novoSensor()
#print("Novo sensor BPM: " + novoSensor.bpm)
