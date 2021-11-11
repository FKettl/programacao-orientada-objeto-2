'''Crie as classes necessárias para um sistema de gerenciamento de uma biblioteca. Os
bibliotecários deverão preencher o sistema com o título do livro, os autores, o ano, a editora, a
edição e o volume. A biblioteca também terá um sistema de pesquisa (outro software), portanto
será necessário conseguir acessar os atributos típicos de pesquisa (nome, autor, …).
'''

class Livro:
    storage = []

    def __init__(self, titulo, autores, ano, editora, edicao = 1, volume = 1):
        self.__titulo = titulo
        self.__autores = autores
        self.__ano = ano
        self.__editora = editora
        self.__edicao = edicao
        self.__volume = volume
        Livro.storage.append(self)
        

    @property
    def titulo(self):
        return self.__titulo


    @property
    def autores(self):
        return self.__autores


    @property
    def ano(self):
        return self.__ano


    @property
    def editora(self):
        return self.__editora


    @property
    def edicao(self):
        return self.__edicao


    @property
    def volume(self):
        return self.__volume

    def remover_livro(self):
        del Livro.storage[self]
    
    @classmethod
    def exibir_storage(cls):
        count = 0
        for x in cls.storage:
            print(f'{count} - {x.titulo}')
            count +=1

livro1 = Livro('O clã dos magos: a Trilogia do Mago Negro', 'Trudi Canavan', 2012, 'Novo Conceito', 1, 1)
livro2 = Livro('A aprendiz: a Trilogia do Mago Negro', 'Trudi Canavan', 2012, 'Novo Conceito', 1, 2)
livro3 = Livro('O lorde supremo: a Trilogia do Mago Negro','Trudi Canavan', 2012, 'Novo Conceito', 1, 2)

Livro.exibir_storage()
print(Livro.storage[2].titulo, '-', Livro.storage[2].autores)
