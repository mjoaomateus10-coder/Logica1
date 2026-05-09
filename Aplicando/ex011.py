secreto = 7
tentativa = 0

while tentativa != secreto:
    tentativa = int(input("Adivinhe o número: "))
    if tentativa < secreto:
        print("Muito baixo!")
    elif tentativa > secreto:
        print("Muito alto!")

print("Acertou!")