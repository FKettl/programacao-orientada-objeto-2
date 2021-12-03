from mamifero import Mamifero


class Gato(Mamifero):

    def __init__(self, volume_som: int = 2, tamanhoPasso: int = 2):
        super().__init__(volume_som, tamanhoPasso)

    def miar(self):
        return f'MAMIFERO: PRODUZ SOM: {self.volume_som} SOM: MIAU'

    def produzirSom(self):
        pass
