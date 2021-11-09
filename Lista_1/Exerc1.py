'''Exercício 1: Banco
O banco Tatu, moderno e eficiente, precisa de um novo programa para controlar o saldo de
seus correntistas. Cada conta corrente pode ter um ou mais clientes como titular. O banco
controla apenas o nome e o telefone de cada cliente. A conta corrente apresenta um saldo e
uma lista de operações de saques e depósitos. Quando o cliente fizer um saque, diminuiremos
o saldo da conta corrente. Quando ele fizer um depósito, aumentaremos o saldo. O banco
oferece também contas especiais, com limite especial além do saldo, e conta poupança, que
oferece um rendimento mensal sempre que o saldo na conta completa um mês. Evidentemente
é necessário oferecer aos clientes a possibilidade de verificar saldos, extratos e um resumo
com todas as informações da conta e seus respectivos clientes'''
import datetime
data = datetime.date.today()

class Conta:

    def __init__(self, saldo = 0, titular = []):
        self.__saldo = saldo
        self.__titular = titular
        self.__historico = [saldo, data]

    @property
    def saldo(self):
        return self.__saldo

    @property
    def historico(self):
        return self.__historico

    @saldo.setter
    def saldo(self, valor):
        self.__saldo += valor
    
    @historico.setter
    def historico(self, lista):
        self.__historico.append(lista)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.append([f'-{valor}'])
            self.historico.append(data)
        else:
            print('Saldo insuficiente')


    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append([f'+{valor}', data])
        else:
            print('Valor incorreto')

    @property
    def titular(self):
        return self.__titular


    def extrato(self):
        print(self.titular, self.saldo)
        for x in self.__historico:
            print(x)



class Poupanca(Conta):

    def __init__(self, saldo=0, titular=[]):
        super().__init__(saldo=saldo, titular=titular)
        

    @property
    def saldo(self):
        return super().saldo


    @property
    def historico(self):
        return super().historico


    @saldo.setter
    def saldo(self, valor):
        valor = int(valor)
        super(Poupanca, type(self)).saldo.fset(self, valor)
    

    @historico.setter
    def historico(self, lista):
        super(Poupanca, type(self)).historico.fset(self, lista)


    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.append([f'-{valor}', data])
        else:
            print('Saldo insuficiente')


    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append([f'+{valor}', data])
        else:
            print('Valor incorreto')


class Conta_Especial(Conta):

    def __init__(self, saldo=0, titular=[], limite_especial = 100):
        super().__init__(saldo=saldo, titular=titular)
        self.limite_especial = limite_especial


    @property
    def saldo(self):
        return super().saldo


    @property
    def historico(self):
        return super().historico


    @saldo.setter
    def saldo(self, valor):
        valor = int(valor)
        super(Conta_Especial, type(self)).saldo.fset(self, valor)
    

    @historico.setter
    def historico(self, lista):
        super(Conta_Especial, type(self)).historico.fset(self, lista)


    def sacar(self, valor):
        if self.saldo+self.limite_especial >= valor:
            self.saldo -= valor
            self.historico.append([f'-{valor}', data])
        else:
            print('Saldo insuficiente')


    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append([f'+{valor}', data])
        else:
            print('Valor incorreto')
  
    


conta1 = Conta_Especial(100)
conta1.depositar(50)
conta1.sacar(200) 
conta1.extrato()

