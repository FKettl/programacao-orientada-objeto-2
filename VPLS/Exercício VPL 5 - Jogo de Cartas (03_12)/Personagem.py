from Interfaces.AbstractPersonagem import *


class Personagem(AbstractPersonagem):

    def __init__(self, energia: int, habilidade: int,
                 velocidade: int, resistencia: int, tipo: Tipo):
        self.__energia = energia
        self.__habilidade = habilidade
        self.__velocidade = velocidade
        self.__resistencia = resistencia
        self.__tipo = tipo

    @property
    def tipo(self) -> Tipo:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def energia(self) -> int:
        return self.__energia

    @energia.setter
    def energia(self, energia):
        self.__energia = energia

    @property
    def habilidade(self) -> int:
        return self.__habilidade

    @habilidade.setter
    def habilidade(self, habilidade):
        self.__habilidade = habilidade

    @property
    def velocidade(self) -> int:
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    @property
    def resistencia(self) -> int:
        return self.__resistencia

    @resistencia.setter
    def resistencia(self, resistencia):
        self.__resistencia = resistencia
