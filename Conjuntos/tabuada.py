# ========================================
# EXERCÍCIO 1 - TABUADA
# ========================================
print("=" * 50)
print("EXERCÍCIO 1 - TABUADA DO 7")
print("=" * 50)

numero = 7

print(f"Tabuada do {numero}:\n")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print()