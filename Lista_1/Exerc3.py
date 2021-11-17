'''Implemente uma classe que, implementa algumas séries matemáticas importantes: Fibonacci,
Fatorial, Fibonarial, Primo. Use recursão para Fibonacci e Fatorial'''

class Matematica:

    def fatorial(numero):
        if numero == 0:
            resultado = 1
        else:
            resultado = numero * Matematica.fatorial(numero-1)

        return resultado

    def lista_fatorial(numero):
        lista = []
        for x in range(numero+1):
            lista.append(Matematica.fatorial(x))

        return lista
    
    def fibonacci(numero):
        if numero == 0:
            resultado = 0
            
        elif numero == 1:
            resultado = 1
            
        else:
            resultado = Matematica.fibonacci(numero-1) + Matematica.fibonacci(numero-2)
        
        return resultado

    def lista_fibonacci(numero):
        lista = []
        for x in range(numero+1):
            lista.append(Matematica.fibonacci(x))

        return lista

    def fibonarial(numero):
        lista = Matematica.lista_fibonacci(numero)
        total = 1
        for x in lista:
            if x > 0:
                total *= x

        return total
        

    def check_primo(numero):
        primo = True
        for x in range(2, numero):
            if (numero%x) == 0:
                primo = False
                break
        
        return primo

    def lista_primo(numero):
        lista = []
        count = 2
        while len(lista) != numero:
            if Matematica.check_primo(count):
                lista.append(count)
            count +=1
        
        return lista




