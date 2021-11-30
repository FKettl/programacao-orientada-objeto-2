from abc import abstractmethod
from animal import Animal


class Mamifero(Animal): 
    
    def __init__(self, volume_som: int, tamanhoPasso: int):
        super().__init__(tamanhoPasso)
        self.__volume_som = volume_som

    @property
    def volume_som(self):
        return self.__volume_som

    @volume_som.setter
    def volume_som(self, volume_som):
        self.__volume_som = volume_som

    @abstractmethod
    def produzirSom(self):
        pass
