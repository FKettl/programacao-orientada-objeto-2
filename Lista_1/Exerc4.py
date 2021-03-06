'''Implemente um sistema de leitura online que possua as seguintes funcionalidades:
● Criação e gerenciamento de usuários
● Busca pelos livros disponíveis (reutilizar classes do exercício 2)
● Leitura de livro (página por página)
○ Apenas um usuário por vez
○ Apenas um livro ativo por usuário
A implementação dos métodos referentes a visualização na tela (display) podem ser
substituídos por um comentário dentro do métodos, ex. “”” atualiza elementoX na tela “””'''
from Exerc2 import *


class Usuario:

    lista_de_usuarios = []

    def __init__(self, nomedeusuario, senha):
        self.__nome = nomedeusuario
        self.__senha = senha
        Usuario.lista_de_usuarios.append(self)
    

    @property
    def nome(self):
        return self.__nome
    

    @nome.setter
    def nome(self, novonome):
        self.__nome = novonome


    @property
    def senha(self):
        return self.__senha


    @senha.setter
    def senha(self, novasenha):
        self.__senha = novasenha


    def deletar_usuario(self):
        index = Usuario.lista_de_usuarios.index(self)
        del Usuario.lista_de_usuarios[index]


class Sistema:

    #inicia quando o usuario baixa o app
    def __init__(self, nomedosistema):
        self.nome = nomedosistema
        self.login = False
        self.livroaberto = False


    def logar(self, usuario, senha):
        Sistema.atualizar_Tela()
        if self.login == True:
            print('Um usuário ja está logado')
        else:
            for x in Usuario.lista_de_usuarios:
                if x.nome == usuario and x.senha == senha:
                    self.login = True
                    print('login com sucesso')
                    break
            if self.login == False:
                print('Usuário e/ou senha estão errados')


    def deslogar(self):
        if self.login == True:
            self.login = False
        else:
            print('Não há um usuário logado')    

    @staticmethod
    def listar_livros():
        Livro.exibir_storage()

    
    def escolher_livro(self):
        if self.livroaberto == True:
            print('Um livro ja está aberto, feche ele primeiro')

        else:
            Sistema.atualizar_Tela()
            livro = input('Escolha um livro(index da lista ou nome): ')
            if livro.isnumeric():
                livro = int(livro)
                '''Mostra o livro'''
                Sistema.atualizar_Tela()
                self.livroaberto = True
                #aqui vai retorna só o objeto, no sistema verdadeiro ia dar pra acessar os atributos, incluindo conteudo 
                return Livro.storage[livro]
            else:
                for x in Livro.storage:
                    if x.titulo == livro:
                        Sistema.atualizar_Tela()
                        self.livroaberto = True
                        '''Mostra o livro'''
                        #aqui vai retorna só o objeto, no sistema verdadeiro ia dar pra acessar os atributos, incluindo conteudo²
                        return x
                print('Livro não encontrado, tente novamente')


    def fechar_livro(self):
        if self.livroaberto == True:
            self.livroaberto = False
            Sistema.atualizar_Tela()
            '''Fecha o livro'''
        else:
            print('Não há um livro aberto')
    

    def proxima_pagina():
        #não coloquei condição de haver um livro aberto pois teoricamente só tem como acessar essa função na tela do livro ja
        Sistema.atualizar_Tela()
        '''Avança a pagina do livro'''


    def voltar_pagina():
        #não coloquei condição de haver um livro aberto pois teoricamente só tem como acessar essa função na tela do livro ja²
        Sistema.atualizar_Tela()
        '''Volta a pagina do livro'''


    def atualizar_Tela():
        '''Pega a ação e atualiza a tela com base nela'''
        print('Tela mudou')


os1 = Sistema('Meu livro')
os1.listar_livros()
print(os1.escolher_livro())