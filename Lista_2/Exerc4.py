'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
consoantes foram lidas. Imprima as consoantes.
'''
letras = [x for x in input('Digite 10 letras(em apenas uma linha): ').split()]
letraslista = []
n = 0
x = 0
#Para caso alguma letra seja digitada sem espaço por exemplo: "asfg a b g h as"
for x in range(len(letras)):
    if len(letras[x])> 1:
        novas = list(letras[x])
        for y in novas:    
            letraslista.append(y)
    else:
        letraslista.append(letras[x])

#aqui letraslista vai ser uma lista de todas as letras separadas
for x in letraslista:
    if x.lower() in 'aeiou':
        letraslista.remove(x)
        
print(f'há um total de {len(letraslista)} consoantes')
print(letraslista)