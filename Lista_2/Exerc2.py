''' Faça um Programa que leia um vetor de 10 números reais e mostre-os na
ordem inversa.
'''
vetor = [float(x) for x in input('Digite o vetor de números reais(uma só linha): ').split()]
print(vetor)
count = len(vetor)
vetor.sort(reverse= True)
for x in vetor:
    print(f'{count}º elemento - {x:.2f}')
    count -= 1