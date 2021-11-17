'''Crie um sistema que gerencia o cadastro de alunos e professores em turmas. Os usuários
serão os membros da secretaria. Eles devem conseguir visualizar os alunos matriculados em
cada turma, com seus dados, suas notas e presenças. Além disso, os secretários precisam ter
acesso a dados cadastrais dos professores associados à disciplina.
'''

class Aluno:

    def __init__(self, nome, matricula, turmas = [], notas = {}, presencas = {} ):
        self.nome = nome
        self.__matricula = matricula
        self.__turmas = turmas
        self.__notas = notas
        self.__presencas = presencas


    @property
    def matricula(self):
        return self.__matricula


    @property
    def turmas(self):
        return self.__turmas


    @turmas.setter
    def turmas(self, turma):
        self.__turmas = turma


    def adicionar_turma(self, turma):
        if turma in self.__turmas:
            print('Esse aluno ja está nessa turma')
        else:
            self.__turmas.append(turma)


    def remover_turma(self, turma):
        if turma in self.__turmas:
            self.__turmas.remove(turma)
        else:
            print('Esse aluno não é desta turma')


    @property
    def notas(self):
        return self.__notas


    def adicionar_nota(self, nota, turma):
        if turma in self.__turmas:
            if nota in self.__notas:
                self.__notas[turma.materia] = self.__notas[turma.materia] + [nota]
            else:
                self.__notas[turma.materia] = [nota]
        else:
            print('Esse aluno não é desta turma')


    @property
    def presencas(self):
        return self.__presencas


    def adicionar_presenca(self, turma):
        if turma in self.__presencas:
            self.__presencas[turma] += 1
        else:
            print('Esse aluno não faz parte dessa turma')


    def remover_presenca(self, turma):
        if turma in self.__presencas :
            if self.__presenca[turma] >= 1:
                self.__presencas[turma] -= 1
        else:
            print('Esse aluno não faz parte dessa turma')


class Professor:

    def __init__(self, nome, turmas = [], id = 0):
        self.nome = nome
        self.__turmas = turmas
        self.id = id


    @property
    def turmas(self):
        return self.__turmas


    def adicionar_turma(self, turma):
        if turma not in self.__turmas:
            self.__turmas.append(turma)
        else:
            print('Esse professor ja da aula pra essa turma')


    def remover_turma(self, turma):
        if turma in self.__turmas:
            self.__turmas.remove(turma)
        else:
            print('Esse professor não da aula pra essa turma')

class Turmas:

    def __init__(self, alunostotal, materia):
        self.alunostotal = alunostotal
        self.materia = materia

class Gerencia:

    def __init__(self, alunos = [], professores = [], turmas = []):
        self.alunos = alunos
        self.professores = professores
        self.turmas = turmas

    def mostrar_alunos(self):
        for x in self.alunos:
            print(x.nome)

    def mostrar_professores(self):
        for x in self.professores:
            print(x.nome)
    
    def mostrar_turmas(self):
        for x in self.turmas:
            print(x.materia)

    def dados_aluno(self, aluno):
        print(aluno.nome, aluno.matricula, [x.materia for x in aluno.turmas], aluno.notas)

    def dados_professor(self, professor):
        print(f'{professor.nome}, {professor.id}, {[x.materia for x in professor.turmas]}')

