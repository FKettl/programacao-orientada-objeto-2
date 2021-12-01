'''Escreva uma função que conta a frequência de ocorrência de cada
palavra em um texto (arquivo txt) e armazena tal quantidade em um dicionário, onde a
chave é a vogal considerada.'''
#Eu ia utilizar regex, porém troquei regex por lógica básica pra fazer a função certinho

def contar_ocorrencia(lista):
    dicionario = {}
    for x in lista:
        if x in dicionario:
            dicionario[x] += 1
        else:
            dicionario[x] = 1
    return dicionario

f = open('C:/1Principal/Projects/Python/POO2/Lista_3/texto.txt', 'r',encoding='utf-8')
conteudo = f.read().lower()
conteudo = conteudo.replace(',', '')
conteudo = conteudo.replace('.', '')
lista = conteudo.split()
dicionario = contar_ocorrencia(lista)
ordenado = sorted(dicionario.items(), key=lambda x: x[1], reverse=True)
print(dicionario)
#Pra ver uma lista de tupla com (palavra, frequencia dela) em ordem decrescente
#print(ordenado)