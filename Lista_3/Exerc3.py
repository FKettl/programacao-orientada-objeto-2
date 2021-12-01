'''Escreva um programa que lê duas notas de vários alunos e armazena tais
notas em um dicionário, onde a chave é o nome do aluno. A entrada de dados deve
terminar quando for lida uma string vazia como nome. Escreva uma função que retorna
a média do aluno, dado seu nome.'''

#fiz de uma forma a funcionar com qualquer quantidade de notas
def retorna_media(nome, dicio):
    notas = dicio[nome]
    media = 0
    for x in notas:
        media += x
    media = media/len(notas)
    return media

dicio = {}

while True:
    nome = input('Digite o nome do aluno: ')
    if not nome:
        break
    nota1, nota2 = [int(x) for x in input('Digite as duas notas dele: ').split()]
    dicio[nome] = [nota1, nota2]
    """
    ia utilizar try/except porém não soube como para o teste no terminal kkk
    try:

    except EOFError:
        break  
    """
