from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:

    def __init__(self, codigo: int, titulo: str,
                 ano: int, editora: Editora, autor: Autor,
                 numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = []
        self.incluirAutor(autor)
        self.capitulos = []
        self.incluirCapitulo(numeroCapitulo, tituloCapitulo)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def ano(self):
        return self.__ano

    @property
    def editora(self):
        return self.__editora

    @property
    def autores(self):
        return self.__autores

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    @autores.setter
    def autores(self, autores):
        self.__autores = autores

    def incluirAutor(self, autor: Autor):
        if (autor not in self.__autores) and (isinstance(autor, Autor)):
            self.__autores.append(autor)

    def excluirAutor(self, autor: Autor):
        if (autor in self.__autores) and (isinstance(autor, Autor)):
            self.__autores.remove(autor)

    def incluirCapitulo(self, numeroCapitulo, tituloCapitulo: str):
        esta = False
        if len(self.capitulos) >= 1:
            for x in self.capitulos:
                if tituloCapitulo == x.titulo:
                    esta = True
        if esta is False:
            capitulo = Capitulo(numeroCapitulo, tituloCapitulo)
            self.capitulos.append(capitulo)

    def excluirCapitulo(self, tituloCapitulo: str):
        esta = False
        if len(self.capitulos) >= 1:
            for x in self.capitulos:
                if tituloCapitulo == x.titulo:
                    objeto = x
                    esta = True
        if esta is True:
            self.capitulos.remove(objeto)

    def findCapituloByTitulo(self, tituloCapitulo: str):
        for x in self.capitulos:
            if x.titulo == tituloCapitulo:
                return x
