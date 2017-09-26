from enum import Enum
import pressao

# When I uncomment this section below, code works. That's all the code in pressao.py
"""class Pressao(Enum):
    NORMAL = 0
    BAIXA = 1
    ALTA = 2"""

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

a = Sensor()

#Says object takes no parameters in python3 and constructor takes no arguments in python 2
foo = Sensor(100, True, "bar")

a.bmp = 100
print(a.bmp)

#Says Pressao is not defined. However, if I uncomment the code above, it does work.
a.pressao = Pressao.NORMAL
print( a.pressao)


