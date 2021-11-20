''' Faça um Programa que leia 4 notas, mostre as notas e a média na tela'''
total = 0.0
notas = []
count = 1

for x in range(4):
    nota = float(input('Digite uma nota: '))
    notas.append(nota)
    total += nota

media = total/4

for x in notas:
    print(f'{count}º elemento - {x:.1f}')
    count += 1
print(f'A média das notas foi: {media:.1f} (Arredondado)')
