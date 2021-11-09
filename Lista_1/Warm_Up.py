 #Warm up 1, 2, 3, 4, 5 e 6:
class Televisao:
    #Warm up 1, 2 e 5:
    def __init__(self, marca = "", tamanho = 16, ligada = False, canal = 2, canal_minimo = 2, canal_maximo = 14):
        self.marca = marca
        self.tamanho = tamanho
        self.ligada = ligada
        self.canal = canal
    #warm up 4:
        self.canal_minimo = canal_minimo
        self.canal_maximo = canal_maximo

    #Warm up 3 e 4:
    def muda_canal_para_cima(self):
        if self.canal == self.canal_maximo:
            self.canal = self.canal_minimo
        else:
            self.canal +=1

    #Warm up 3 e 4:
    def muda_canal_para_baixo(self):
        if self.canal == self.canal_minimo:
            self.canal = self.canal_maximo
        else:
            self.canal -= 1
    



#Warm up 1 e 2
'''tv1 = Televisao('LG', 46, False, 10)
tv2 = Televisao('Toshiba', 32, True, 6)

print(tv1.marca)
print(tv2.marca)
print(tv1.tamanho)
print(tv2.tamanho)'''

#warm up 6:
'''tv1 = Televisao('Samsung', 32, False, 5)
tv2 = Televisao('Sonic', 48, True, 8)
tv1.canal_minimo = 3
tv1.canal_maximo = 10
tv2.canal_minimo = 1
tv2.canal_maximo = 8
'''

#warm up 7:
class Estados:

    def __init__(self, nome = "", sigla = "", cidades = []):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades
        self.populacao = self.populacao_total()


    def populacao_total(self):
        total = 0
        for x in self.cidades:
            total += x.populacao
        return total

#warm up 7:
class Cidades:

    def __init__(self, nome = "", populacao = 0):
        self.nome = nome
        self.populacao = populacao

#warm up 7:
'''
cidade1 = Cidades('Erechim', 100000)  
cidade2 = Cidades('Passo Fundo', 150000)
cidade3 = Cidades('Porto Alegre', 1500000)
cidade4 = Cidades('Florianopolis', 500000)
cidade5 = Cidades('Piratuba', 15000)
cidade6 = Cidades('Rio de janeiro', 2000000)

rioGrandeDoSul = Estados('Rio Grande Do Sul', 'RS', [cidade1, cidade2, cidade3])
santaCatarina = Estados('Santa Catarina', 'SC', [cidade4, cidade5])
rioDeJaneiro = Estados('Rio De Janeiro', 'RJ', [cidade6])

print(rioGrandeDoSul.populacao)
print(santaCatarina.populacao)
print(rioDeJaneiro.populacao)
'''

#warm up 8:
from math import sqrt, atan2

class Coordenada:
        
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
  

    def mostrar_coordenadas(self):
        coordenadas = f'({self.x}, {self.y})'

        return coordenadas

    
    def mostrar_forma_polar(self):
        x = self.x
        y = self.y
        r = sqrt(x^2 + y^2)
        sigma = atan2(y, x)
        polar = f'{r} cos({sigma:.2f}),{r} sin({sigma:.2f})'
        
        return polar


    @staticmethod
    def calcular_distancia(coord1, coord2):
        x = abs(coord1.x - coord2.x)
        y = abs(coord1.y - coord2.y)
        distancia = sqrt(x^2 + y^2)

        return f'{distancia:.2f}'

    
    @staticmethod
    def comparar_coordenadas(coord1, coord2):
        isequal = False
        if (coord1.y == coord2.y) and (coord1.x == coord2.x):
            isequal = True
        
        return isequal

  
'''
coord1 = Coordenada(5, 10)
coord2 = Coordenada(2, 6)
print(coord1.mostrar_forma_polar())
'''

#warm up 9

class Quadrado:

    def __init__(self, lado):
        self.lado = lado
        self.area = Quadrado.calc_area()


    def calc_area(self):
        area = self.lado**2

        return area

class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.area = Triangulo.calc_area()

    def calc_area(self):
        semip = (self.lado1 + self.lado2 + self.lado3)/2
        area = sqrt(semip*(semip-self.lado1)*(semip-self.lado2)*(semip*self.lado3))
        
        return area

class Circulo:
    
    def __init__(self, raio):
        self.raio = raio
        self.area = Circulo.calc_area()

    def calc_area(self):
        pi = 3.1415
        area = pi*(self.raio**2)

        return area

#warm up 10

class Fracao:

    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        self.denominador = int(denominador)

    @staticmethod
    def somar(fracao1, fracao2):
        numerador1 = fracao1.numerador
        denominador1 = fracao1.denominador
        numerador2 = fracao2.numerador
        denominador2 = fracao2.denominador
        numeradorfinal = (numerador1*denominador2) + (numerador2*denominador1)
        denominadorfinal = (denominador1*denominador2)

        return numeradorfinal, denominadorfinal

    @staticmethod
    def subtrair(fracao1, fracao2):
        numerador1 = fracao1.numerador
        denominador1 = fracao1.denominador
        numerador2 = fracao2.numerador
        denominador2 = fracao2.denominador
        numeradorfinal = (numerador1*denominador2) - (numerador2*denominador1)
        denominadorfinal = (denominador1*denominador2)

        return numeradorfinal, denominadorfinal


    @staticmethod
    def multiplicar(fracao1, fracao2):
        numerador1 = fracao1.numerador
        denominador1 = fracao1.denominador
        numerador2 = fracao2.numerador
        denominador2 = fracao2.denominador
        numeradorfinal = (numerador1*numerador2)
        denominadorfinal = (denominador1*denominador2)

        return numeradorfinal, denominadorfinal


    @staticmethod
    def dividir(fracao1, fracao2):
        numerador1 = fracao1.numerador
        denominador1 = fracao1.denominador
        numerador2 = fracao2.numerador
        denominador2 = fracao2.denominador
        numeradorfinal = (numerador1*denominador2)
        denominadorfinal = (denominador1*numerador2)

        return numeradorfinal, denominadorfinal


    def printar_fracao(self):
        numerador = self.numerador
        denominador = self.denominador

        print(f'{numerador}')
        print('-'*len(str(numerador)))
        print(f'{denominador}')


    def inverte_fracao(self):
        numerador = self.denominador
        denominador = self.numerador

        return numerador, denominador


    def retorna_valor_real(self):
        numerador = self.numerador
        denominador = self.denominador
        valor = numerador/denominador

        return valor

    @staticmethod
    def cria_fracao(numero):
        numero = str(numero)
        inutil, casasAposAVirgula = numero.split('.')
        numerador = float(numero)*10**len(str(casasAposAVirgula))
        denominador = 10**len(str(casasAposAVirgula))

        return numerador, denominador

'''
f1 = Fracao(10, 5)
f2 = Fracao(1,2)
print(Fracao.cria_fracao(1250.55))'''