from sensor import *

listaSensores = []

def novoSensor():
    novoSensor = Sensor()
    getValores(novoSensor)
    listaSensores.append(novoSensor)

def enviarValores():

    #Imprimindo os sensores
    for a in listaSensores:
        print(a.bmp)
        print(a.movimento)
        print(a.pressao)


#Criando 5 sensores
for i in range (5):
    novoSensor()

for i in range (5):
    enviarValores()






