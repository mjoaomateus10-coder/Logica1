numeros = []

for i in range(5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

maior = max(numeros)

print(f'Maior número: {maior}')