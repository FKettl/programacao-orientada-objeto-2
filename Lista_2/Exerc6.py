'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e
armazene num vetor a média de cada aluno, imprima o número de alunos com média
maior ou igual a 7.0.'''
medias = []
count = 0
for x in range(10):
    media = 0
    notas = [float(x) for x in input(f'Digite as 4 notas do {x+1}º aluno: ').split()]
    for x in notas:
        media += x
    media = media/4
    medias.append(media)
for x in medias:
    if x >= 7.0:
        count +=1

print(f'Há {count} alunos com média maior ou igual a 7.0')