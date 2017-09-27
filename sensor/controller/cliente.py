import sys
sys.path.insert(0, '/home/guiga/Desktop/Guiga/UEFEY/5_semestre_Redes/MI/P1/sensor/model')

from sensor import *

""" Classe correspondente ao controller de sensores, pra ser usada na interface que simula um sensor
    Responsavel por comunicar o model de sensor com a interface
"""

#Cria um novo sensor e atribui valores aleatorios a ele
def novoSensor():
    novoSensor = Sensor()
    novoSensor.getValores()
    return novoSensor


def enviarValores(sensor):
    #Imprimindo os sensores
    print(sensor.bpm)
    print(sensor.movimento)
    print(sensor.pressao)


###Teste

#Criando 5 sensores
novoSensor = novoSensor()
    
for i in range (5):
    enviarValores(novoSensor)    
    novoSensor.getValores()





