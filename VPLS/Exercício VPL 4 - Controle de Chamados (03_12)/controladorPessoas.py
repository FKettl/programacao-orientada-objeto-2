from typing import List
from interfaces.abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):

    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def incluiCliente(self, codigo: int, nome: str) -> Cliente:
        jaexiste = False
        for x in self.clientes:
            if codigo == x.codigo:
                jaexiste = True
                break
        if not jaexiste:
            cliente = Cliente(nome, codigo)
            self.__clientes.append(cliente)
            return cliente

    def incluiTecnico(self, codigo: int, nome: str) -> Tecnico:
        existe = False
        for x in self.tecnicos:
            if codigo == x.codigo:
                existe = True
                break
        if not existe:
            tecnico = Tecnico(nome, codigo)
            self.__tecnicos.append(tecnico)
            return tecnico
