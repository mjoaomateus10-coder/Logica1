# Criando uma lista

compras = []

for i in range(3):
    item = input('Digite um item da compra: ')
    compras.append(item)

print('\nLista de compras:')

for produto in compras:
    print(produto)