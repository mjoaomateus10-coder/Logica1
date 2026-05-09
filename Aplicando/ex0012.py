numero = 7

for i in range(1, 11):
    resultado = numero * i
    if resultado > 50:
        print(f"{numero} x {i} = {resultado} ⚠️ (maior que 50)")
    else:
        print(f"{numero} x {i} = {resultado}")