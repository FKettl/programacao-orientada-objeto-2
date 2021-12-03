from abc import ABC, abstractmethod
from Carta import *
from Interfaces import AbstractJogador
import random


class Jogador(AbstractJogador):

    def __init__(self, nome: str):
        self.__nome = nome
        self.__mao = []

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def mao(self) -> list:
        return self.__mao

    @mao.setter
    def mao(self, mao):
        self.__mao = mao

    def baixa_carta_da_mao(self) -> Carta:
        numero = random.randint(0, len(self.mao))
        carta = self.__mao.pop()
        return carta

    def inclui_carta_na_mao(self, carta:Carta):
        if isinstance(carta, Carta):
            self.__mao.append(carta)
