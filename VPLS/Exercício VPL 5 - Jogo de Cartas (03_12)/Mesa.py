from Interfaces import AbstractMesa
from Carta import *
from Jogador import *


class Mesa(AbstractMesa):

    def __init__(self, jogador1: Jogador, jogador2: Jogador,
                 cartaJogador1: Carta, cartaJogador2: Carta):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        self.__carta_jogador1 = cartaJogador1
        self.__carta_jogador2 = cartaJogador2

    @property
    def jogador1(self) -> Jogador:
        return self.__jogador1

    @jogador1.setter
    def jogador1(self, jogador1):
        self.__jogador1 = jogador1

    @property
    def jogador2(self) -> Jogador:
        return self.__jogador2

    @jogador2.setter
    def jogador2(self, jogador2):
        self.__jogador2 = jogador2

    @property
    def carta_jogador1(self) -> Carta:
        return self.__carta_jogador1

    @carta_jogador1.setter
    def carta_jogador1(self, carta_jogador1):
        self.__carta_jogador1 = carta_jogador1

    @property
    def carta_jogador2(self) -> Carta:
        return self.__carta_jogador2

    @carta_jogador2.setter
    def carta_jogador2(self, carta_jogador2):
        self.__carta_jogador2 = carta_jogador2
