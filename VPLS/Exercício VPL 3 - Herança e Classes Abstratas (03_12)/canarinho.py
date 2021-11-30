from ave import Ave


class Canarinho(Ave):

    def __init__(self, tamanhoPasso: int, altura_voo: int):
        super().__init__(tamanhoPasso, altura_voo)

    def cantar(self):
        return "AVE: PRODUZ SOM: PIU"

    def produzirSom(self):
        pass
