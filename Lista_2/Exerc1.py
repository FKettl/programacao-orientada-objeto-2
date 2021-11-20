'''Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.'''
#Assumi que por ser UM vetor então a input sera uma linha, por exemplo: "2 4 6 3 1"
vetor = [int(x) for x in input('Digite o vetor de inteiros(uma só linha): ').split()]
print(vetor)
count = 1
for x in vetor:
    print(f'{count}º elemento - {x}')
    count += 1