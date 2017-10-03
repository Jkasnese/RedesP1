#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
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
    caracterSeperador = ';'
    mensagem = str(sensor.bpm) + caracterSeparador
    mensagem += str(sensor.movimento) + caracterSeparador
    mensagem += str(sensor.pressao) + caracterSeparador
    return mensagem


def enviarValores(sensor):
    """ Envia valores aleatorios continuamente ate o usuario modificar o valor.
    A partir dai, envia os valores definidos pelo usuario"""

    while(True):
        print("Entrou no loopenviar")
        time.sleep(1)
        if (novoSensor.modificado == False):
            novoSensor.gerarValores()
            enviarUDP(UDP_IP, selecionaValores(sensor))
        else:
            enviarUDP(UDP_IP, selecionaValores(sensor))
            # Remover esse breal depois
            break; 

def cadastrarSensor(sensor):
    mensagem = "0" + sensor.cpf
    resposta = "1"
    while (resposta != "0"):
        UDP_PORT = int(input("Digite a porta para recebimento: "))
        enviarUDP(UDP_IP, mensagem)
        print ("Enviado: ", mensagem)
        resposta = ouvirUDP(abrirSocketUDP(UDP_PORT))
        print("Resposta: ", resposta)

def novoSensor():
    cpf = input("Digite o CPF do sensor: ")
    novoSensor = Sensor(cpf)
    novoSensor.gerarValores()
    # Cadastrar sensor no servidor
    cadastrarSensor(novoSensor)
    print("Sensor cadastrado!")
    # Depois de cadastrado, começar a enviar valores
    #threadEnviaValores = Thread(target = enviarValores, args = (novoSensor,))
    #threadEnviaValores.start()
    return novoSensor



###Teste

#Criando Sensor
novoSensor = novoSensor()

# Modificando e enviando
time.sleep(2)
novoSensor.set_Valores(100, 0, 2)
enviarValores(novoSensor)




