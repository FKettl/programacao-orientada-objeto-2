'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere
um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores.'''


vetorA = [int(x) for x in input('Digite um vetor de 10 elementos: ').split()]
vetorB = [int(x) for x in input('Digite outro vetor, tambem de 10 elementos: ').split()]
vetorC = []
for x in range(len(vetorA)):
    vetorC.append(vetorA[x])
    vetorC.append(vetorB[x])

print(vetorC)