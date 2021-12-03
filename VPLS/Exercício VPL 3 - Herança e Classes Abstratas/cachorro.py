from mamifero import Mamifero


class Cachorro(Mamifero):

    def __init__(self, volume_som: int = 3, tamanhoPasso: int = 3):
        super().__init__(volume_som, tamanhoPasso)

    def latir(self):
        return f'MAMIFERO: PRODUZ SOM: {self.volume_som} SOM: AU'

    def produzirSom(self):
        pass
