'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene
cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa
a ordem lida.'''
lista = []
for x in range(5):
    idade, altura = [float(x) for x in input(f'Digite a idade e a altura da primeira {x}º pessoa ').split()]
    idade = int(idade)
    lista.insert(0, [idade, altura])
print()
count = len(lista)
for x in lista:
    print(f"A {count}º pessoa tem {x[0]} anos e {x[1]} metros de altura")
    count -= 1