'''Faça um Programa que leia um vetor A com 10 números inteiros, calcule
e mostre a soma dos quadrados dos elementos do vetor.'''

vetorA = [int(x) for x in input('Digite 10 números inteiros: ').split()]
soma = 0
for x in vetorA:
    soma += x**2
print(f'A soma dos quadrados é {soma}')