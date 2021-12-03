from Interfaces  import AbstractCarta
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    def valor_total_carta(self) -> int:
        charac = self.personagem
        total = (charac.energia
                 + charac.habilidade
                 + charac.resistencia
                 + charac.velocidade)
        return total

    @property
    def personagem(self) -> Personagem:
        return self.__personagem

    @personagem.setter
    def personagem(self, personagem):
        self.__personagem = personagem
