# Programa que soma números até o usuário decidir parar

soma = 0

while True:
    numero = int(input("Digite um número (0 para parar): "))

    if numero == 0:
        break  # sai do loop

    soma += numero  # soma acumulativa

print(f"A soma total foi: {soma}")