from enum import Enum
from pressao import Pressao
import random

class Sensor:
    """Classe responsavel pela definicao dos sensores.
       Atributos:
        int bmp
        bool movimento
        Pressao pressao"""

def __init__(self, bmp, movimento, pressao):
    self.bmp = int(bmp)
    self.movimento = bool(movimento)
    self.pressao = pressao

def getValores(self):
    self.bmp = random.randint(30, 140)
    self.movimento = bool(random.randint(0,1))
    self.pressao = Pressao(random.randint(0,2))


