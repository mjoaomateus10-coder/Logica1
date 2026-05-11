# ========================================
# EXERCÍCIO 3 - SOMA DE NÚMEROS PARES
# ========================================
print("=" * 50)
print("EXERCÍCIO 2 - SOMA DE NÚMEROS PARES")
print("=" * 50)

numeros = [2, 5, 8, 12, 15, 20, 25, 30, 35, 40]
soma_pares = 0
pares_encontrados = []

for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero
        pares_encontrados.append(numero)

print(f"Lista de números: {numeros}")
print(f"Números pares encontrados: {pares_encontrados}")
print(f"Soma dos pares: {soma_pares}")
print(f"Total de pares: {len(pares_encontrados)}")

print()
