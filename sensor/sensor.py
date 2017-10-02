#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum
from pressao import Pressao
import random

# Precisa mudar a pressao pra valores?
# Falta criar ID unico atraves de uma rede network

class Sensor:

    """Classe responsavel pela definicao dos sensores.
       Atributos do objeto:
        int bmp
        bool movimento
        Pressao pressao
        String nome
        bool modificado

       Atributos estaticos ou da classe:
        ID"""

    def __init__(self, nome):
        self.id = 0
        self.nome = nome
        self.bpm = random.randint(30, 140)
        self.movimento = bool(random.randint(0,1))
        self.pressao = Pressao(random.randint(0,2))
        self.modificado = False

    @property
    def bpm(self):
        return self._bpm

    @bpm.setter
    def bpm(self, bpm):
        self._bpm = bpm
        self.modificado = True

    @property
    def movimento(self):
        return self._movimento
    
    @movimento.setter
    def movimento(self, movimento):
        self._movimento = bool(movimento)
        self.modificado = True

    @property
    def pressao(self):
        return self._pressao
    
    @pressao.setter
    def pressao(self, pressao):
        self._pressao = Pressao(pressao)
        self.modificado = True

    def gerarValores(self):
        self.bpm = self.bpm + random.randint(-5, 5)
        self.modificado = False

    def set_Valores(self, bpm, movimento, pressao):
        self.bpm = bpm
        self.movimento = movimento
        self.pressao = pressao
        self.modificado = True
        



