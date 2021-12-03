'''Escreva um programa para armazenar uma agenda de telefones usando
um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o
nome completo da pessoa. Seu programa deve ter as seguintes funções:
incluir_novo_nome – essa função acrescenta um novo nome na agenda, com
um ou mais telefones. Ela deve receber como argumentos o nome e os telefones.
incluir_telefone – essa função acrescenta um telefone em um nome existente na
agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja
incluí- lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo
nome.
excluir_telefone – essa função exclui um telefone de uma pessoa que
já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da
agenda.
excluir_nome – essa função exclui uma pessoa da agenda.
consultar_telefone – essa função retorna os telefones de uma pessoa
na agenda.'''

class Agenda:

    def __init__(self, id) -> None:
        self.__id = id
        self.__agenda = {}
        
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def agenda(self):
        return self.__agenda

    @agenda.setter
    def agenda(self, agenda: dict):
        self.__agenda = agenda

    def incluir_novo_nome(self, nome: str, telefone: list):
        if nome not in self.agenda:
            if not isinstance(telefone, list):
                telefone = [telefone]
            self.agenda[nome] = telefone

    def incluir_telefone(self, nome, telefone):
        if nome not in self.agenda:
            resposta = input('Nome não existe na agenda, deseja inclui-lo? [s/n] ').lower()
            if resposta == 's':
                self.incluir_novo_nome(nome, telefone)
        else:
            if telefone not in self.agenda[nome]:
                if not isinstance(telefone, list):
                    telefone = [telefone]
                self.agenda[nome] = self.agenda[nome] + telefone

    def excluir_telefone(self, telefone):
        for x in self.agenda:
            if telefone in self.agenda[x]:
                if len(self.agenda[x]) == 1:
                    del self.agenda[x]
                    break
                else:
                    self.agenda[x].remove(telefone)
                    break
        
    def excluir_nome(self, nome):
        if nome in self.agenda:
            del self.agenda[nome]

    def consultar_telefone(self, nome):
        if nome in self.agenda:
            for x in self.agenda[nome]:
                print(x)
