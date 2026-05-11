# ========================================
# EXERCÍCIO 4 - COMPRAS COM DESCONTO
# ========================================
print("=" * 50)
print("EXERCÍCIO 4 - CÁLCULO DE COMPRAS COM DESCONTO")
print("=" * 50)

produtos = [
    {"nome": "Notebook", "preco": 2500, "quantidade": 1},
    {"nome": "Mouse", "preco": 80, "quantidade": 3},
    {"nome": "Teclado", "preco": 300, "quantidade": 2},
    {"nome": "Monitor", "preco": 1200, "quantidade": 1}
]

total = 0
itens_caros = []

print("ITENS COMPRADOS:\n")

for produto in produtos:
    subtotal = produto["preco"] * produto["quantidade"]
    total += subtotal
    
    print(f"{produto['nome']}:")
    print(f"  Preço unitário: R${produto['preco']}")
    print(f"  Quantidade: {produto['quantidade']}")
    print(f"  Subtotal: R${subtotal}\n")
    
    if subtotal > 500:
        itens_caros.append(produto["nome"])

print(f"Total sem desconto: R${total:.2f}")

if total > 2000:
    desconto = total * 0.15
    total_final = total - desconto
    desconto_percentual = 15
elif total > 1000:
    desconto = total * 0.10
    total_final = total - desconto
    desconto_percentual = 10
else:
    desconto = 0
    total_final = total
    desconto_percentual = 0

if desconto > 0:
    print(f"Desconto ({desconto_percentual}%): -R${desconto:.2f}")
    print(f"Total com desconto: R${total_final:.2f}")
    print(f"Economia: R${desconto:.2f} ✓")
else:
    print("Nenhum desconto aplicado")

print(f"\nItens com preço acima de R$500: {itens_caros}")

print()