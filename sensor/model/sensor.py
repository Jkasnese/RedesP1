from enum import Enum
from pressao import Pressao
import random

class Sensor:

    """Classe responsavel pela definicao dos sensores.
       Atributos:
        int bmp
        bool movimento
        Pressao pressao"""

    def __init__(self):
        self.bpm = random.randint(30, 140)
        self.movimento = bool(random.randint(0,1))
        self.pressao = Pressao(random.randint(0,2))

    def getValores(self):
        self.bpm = self.bpm + random.randint(-5, 5)



