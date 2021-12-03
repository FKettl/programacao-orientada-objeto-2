from interfaces.abstractTipoChamado import AbstractTipoChamado


class TipoChamado(AbstractTipoChamado):

    def __init__(self, codigo: int, descricao: str, nome: str):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
