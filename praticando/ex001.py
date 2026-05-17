notas = []

for i in range(3):
    nota = float(input('Digite uma nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f'Média: {media:.2f}')

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')