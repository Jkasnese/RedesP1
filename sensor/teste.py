import time
from threading import Thread

def olaMundo():
    while (True):
        print ("Ola mundo")

def helloWorld():
    while(True):
        print ("Hello World")

threadOla = Thread(target = olaMundo,)
threadHello = Thread(target = helloWorld,)

threadOla.start()
threadHello.start()


time.sleep(10)
print("Testando")
time.sleep(2)
print("Falou!")
