from abc import abstractmethod
from animal import Animal


class Ave(Animal):

    def __init__(self, tamanhoPasso: int, altura_voo: int):
        super().__init__(tamanhoPasso)
        self.__altura_voo = altura_voo

    @property
    def altura_voo(self):
        return self.__altura_voo

    @altura_voo.setter
    def altura_voo(self, altura_voo):
        self.__altura_voo

    def mover(self):
        return f'ANIMAL: DESLOCOU {self.tamanho_passo} VOANDO'

    @abstractmethod
    def produzirSom(self):
        pass
