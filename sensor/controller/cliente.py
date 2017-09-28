#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import _thread

#Achar jeito melhor pra importar
import sys
sys.path.insert(0, '/home/guiga/Desktop/Guiga/UEFEY/5_semestre_Redes/MI/P1/sensor/model')

from sensor import *

""" Classe correspondente ao controller de sensores, pra ser usada na interface que simula um sensor
    Responsavel por comunicar o model de sensor com a interface
"""

#Cria um novo sensor e atribui valores aleatorios a ele
def selecionaValores(sensor):
    #Imprimindo os sensores
    print(sensor.id)
    print(sensor.nome)
    print(sensor.bpm)
    print(sensor.movimento)
    print(sensor.pressao)


def enviarValores(sensor):
    """ Envia valores aleatorios continuamente ate o usuario modificar o valor.
    A partir dai, envia os valores definidos pelo usuario"""

    while(True):
        time.sleep(2)
        if (novoSensor.modificado == False):
            selecionaValores(sensor)
            novoSensor.gerarValores()
        else:
            selecionaValores(sensor)
            break; 

def novoSensor():
    novoSensor = Sensor('Buba')
    novoSensor.gerarValores()
    _thread.start_new_thread(enviarValores, (novoSensor,))
    return novoSensor 


###Teste

#Criando Sensor
novoSensor = novoSensor()

# Modificando e enviando
time.sleep(10)
novoSensor.set_Valores(100, 0, 2)
enviarValores(novoSensor)




