"""Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
Escreva um programa que leia todos os tempos em segundos e os guarde em um
dicionário, onde a chave é o nome do corredor. Ao final diga de quem foi a melhor volta
da prova e em que volta; e ainda a classificação final em ordem (1o o campeão). O
campeão é o que tem a menor média de tempos."""

dicio_tempos = {}
classificacao = {}
melhor_tempo = -1
melhor_volta = None
nome_melhor = None

for x in range(3):
    nome = input("Digite o nome do corredor: ")
    tempos = [int(x) for x in input('Digite os 6 tempos desse corredor (todos na mesma linha): ').split()]
    media = sum(tempos)/len(tempos)
    dicio_tempos[nome] = tempos
    classificacao[nome] = media
    for index, x in enumerate(tempos):
        if (x < melhor_tempo) or (melhor_tempo == -1):
            melhor_tempo = x
            melhor_volta = index+1
            nome_melhor = nome

    
print(f'{nome_melhor} teve a volta mais rápida, com um tempo de {melhor_tempo} na {melhor_volta}ª volta')
ordenado = sorted(classificacao.items(), key=lambda x: x[1])
print()
for index, x in enumerate(ordenado):
    print(f'{index+1}º lugar: {x[0]}')
