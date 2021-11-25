'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a
soma, a multiplicação e os números.'''


numero = [int(x) for x in input('Digite um vetor de 5 números inteiros: ').split()]

soma = 0
multiplicacao = 1

for x in numero:
    soma += x
    multiplicacao *= x

print(f'Os números são {numero}')
print(f'A soma deles é {soma}')
print(f'E sua multiplicação é {multiplicacao}')