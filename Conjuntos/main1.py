print("=" * 50)
print("CÓDIGO 3 - CLASSIFICAÇÃO POR IDADE")
print("=" * 50)

pessoa1_nome = "Pedro"
pessoa1_idade = 10

pessoa2_nome = "Ana"
pessoa2_idade = 16

pessoa3_nome = "Carlos"
pessoa3_idade = 30

pessoas = [
    {"nome": pessoa1_nome, "idade": pessoa1_idade},
    {"nome": pessoa2_nome, "idade": pessoa2_idade},
    {"nome": pessoa3_nome, "idade": pessoa3_idade}
]
    
for pessoa in pessoas:
    nome = pessoa["nome"]
    idade = pessoa["idade"]
    
    if idade < 12:
        categoria = "Criança"
    elif idade < 18:
        categoria = "Adolescente"
    else:
        categoria = "Adulto"
    
    print(f"{nome} tem {idade} anos - Categoria: {categoria}")

print("\n" + "=" * 50)
print("✓ CÓDIGOS EXECUTADOS COM SUCESSO!")
print("=" * 50)
