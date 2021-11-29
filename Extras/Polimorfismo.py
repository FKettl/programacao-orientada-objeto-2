from abc import ABC, abstractmethod
       

class Transporte(ABC):
    def __init__(self, nome: str,
                 altura: int, comprimento: int,
                 carga: int, velocidade: int):
        self.__nome = nome
        self.__altura = altura
        self.__comprimento = comprimento
        self.__carga = carga
        self.__velocidade = velocidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def comprimento(self):
        return self.__comprimento
    
    @comprimento.setter
    def comprimento(self, comprimento):
        self.__comprimento = comprimento

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, carga):
        self.__carga = carga

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    def __str__(self):
        return f"Nome: {self.nome}, altura: {self.altura} metros, comprimento: {self.comprimento} metros;"

class TransporteAereo(Transporte):
    def __init__(self, nome: str,
                 altura: int, comprimento: int,
                 carga: int, velocidade: int,
                 autonomia: int, envergadura: int):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__autonomia = autonomia
        self.__envergadura = envergadura

    @property
    def autonomia(self):
        return self.__autonomia

    @autonomia.setter
    def autonomia(self, autonomia):
        self.__autonomia = autonomia

    @property
    def envergadura(self):
        return self.__envergadura

    @envergadura.setter
    def envergadura(self, envergadura):
        self.__envergadura = envergadura

class TransporteTerrestre(Transporte):

    def __init__(self, nome: str,
                 altura: int, comprimento: int,
                 carga: int, velocidade: int,
                 motor: str, rodas: str):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__motor = motor
        self.__rodas = rodas

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, motor):
        self.__motor = motor

    @property
    def rodas(self):
        return self.__rodas
    
    @rodas.setter
    def rodas(self, rodas):
        self.__rodas = rodas

class TransporteAquatico(Transporte):

    def __init__(self, nome: str,
                 altura: int, comprimento: int,
                 carga: int, velocidade: int,
                 boca: int, calado: int):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__boca = boca
        self.__calado = calado

    @property
    def boca(self):
        return self.__boca

    @boca.setter
    def boca(self, boca):
        self.__boca = boca

    @property
    def calado(self):
        return self.__calado

    @calado.setter
    def calado(self, calado):
        self.__calado = calado       


class Catalogo():
    
    def __init__(self, nome: str):
        self.__nome = nome
        self.__transporte_aereo = []
        self.__transporte_terrestre = []
        self.__transporte_aquatico = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def transporte_aereo(self):
        return self.__transporte_aereo

    @transporte_aereo.setter
    def transporte_aereo(self, lista):
        self.__transporte_aereo = lista

    @property
    def transporte_terrestre(self):
        return self.__transporte_terrestre

    @transporte_terrestre.setter
    def transporte_terrestre(self, lista):
        self.__transporte_terrestre = lista

    @property
    def transporte_aquatico(self):
        return self.__transporte_aquatico

    @transporte_aquatico.setter
    def transporte_aquatico(self, lista):
        self.__transporte_aquatico = lista

    def inserção(self, objeto):
        if (objeto not in self.transporte_aquatico) and (objeto not in self.transporte_aereo) and (objeto not in self.transporte_terrestre):
            if isinstance(objeto, TransporteAquatico):
                self.transporte_aquatico.append(objeto)
            elif isinstance(objeto, TransporteAereo):
                self.transporte_aereo.append(objeto)
            elif isinstance(objeto, TransporteTerrestre):
                self.transporte_terrestre.append(objeto)
            else:
                print("Este não é Transporte conhecido.")

    def apresentacao(self):
        print("-- Lista de transporte aquático --")
        for x in self.transporte_aquatico:
            print(x)
        print()
        print("-- Lista de transporte aéreo --")
        for x in self.transporte_aereo:
            print(x)
        print()
        print("-- Lista de transporte terrestre --")
        for x in self.transporte_terrestre:
            print(x)
