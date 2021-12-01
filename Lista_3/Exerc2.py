'''Escreva uma função que apaga do dicionário anterior, todas as palavras
que sejam ‘stopwords ’.'''
from Exerc1 import dicionario

print(len(dicionario))   
e = open('C:/1Principal/Projects/Python/POO2/Lista_3/stopwords.txt', 'r', encoding='utf-8')
stopwords = e.read().lower().split()
for x in stopwords:
    if x in dicionario:
        del dicionario[x]
print(dicionario)