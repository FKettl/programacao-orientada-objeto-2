from types import NoneType
from interfaces.abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):

    def __init__(self):
        self.__chamados = []
        self.__tipos_chamados = []

    @property
    def chamados(self):
        return self.__chamados

    @chamados.setter
    def chamados(self, chamados):
        self.__chamados = chamados

    @property
    def tipoChamados(self):
        return self.__tipos_chamados

    @tipoChamados.setter
    def tipoChamados(self, tipochamados):
        self.__tipos_chamados = tipochamados

    def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
        count = 0
        for x in self.chamados:
            if x.tipo.codigo == tipo.codigo:
                count += 1
        return count

    def incluiChamado(self, data: Date, cliente: Cliente,
                      tecnico: Tecnico, titulo: str,
                      descricao: str, prioridade: int,
                      tipo: TipoChamado) -> Chamado:
        if (isinstance(data, Date) and
                isinstance(cliente, Cliente) and
                isinstance(tecnico, Tecnico) and
                isinstance(tipo, TipoChamado)):
            existe = False
            for x in self.chamados:
                if (x.data == data and
                        x.cliente == cliente and
                        x.tecnico == tecnico and
                        x.tipo == tipo):
                    existe = True
            if not existe:
                chamado = Chamado(data, cliente,
                                  tecnico, titulo,
                                  descricao, prioridade, tipo)
                self.chamados.append(chamado)
                return chamado

    def incluiTipoChamado(self, codigo: int,
                          nome: str, descricao: str) -> TipoChamado:
        existe = False
        for x in self.tipoChamados:
            if x.codigo == codigo:
                existe = True
        if not existe:
            tipochamado = TipoChamado(codigo, descricao, nome)
            self.tipoChamados.append(tipochamado)
            return tipochamado
