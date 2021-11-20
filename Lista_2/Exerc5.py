'''Faça um Programa que leia 20 números inteiros e armazene-os num
vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor
impar. Imprima os três vetores.'''

def ver_par(numero):
    if numero%2 == 0:
        return True
    else:
        return False

numeros = []
par = []
impar = []

for x in range(20):
    numero = int(input('Digite um numero: '))
    numeros.append(numero)
    if ver_par(numero):
        par.append(numero)
    else:
        impar.append(numero)

numeros.sort()
par.sort()
impar.sort()

print(f'Lista de todos os números: {numeros}')
print(f'Lista de números pares: {par}')
print(f'Lista de números ímpares: {impar}')
'''
4
5
6
7
8
99
0
0
452
34
5
3
2
1
312
4
6
8
9
0
32
'''