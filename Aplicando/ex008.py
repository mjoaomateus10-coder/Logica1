# PROGRAMA: Gerenciador de Notas de Alunos

# VARIÁVEIS
nome_escola = "Escola ABC"
alunos = []  # COLEÇÃO (lista vazia)
media_minima = 7

print(f"=== Bem-vindo ao {nome_escola} ===\n")

# LAÇO DE REPETIÇÃO - Pedir dados de 3 alunos
for i in range(3):
    print(f"--- Aluno {i + 1} ---")
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota (0-10): "))
    
    # COLEÇÃO - Armazenar dados em dicionário
    aluno = {
        "nome": nome,
        "nota": nota
    }
    
    alunos.append(aluno)  # Adicionar à lista
    print()

print("\n=== RESULTADO FINAL ===\n")

# LAÇO DE REPETIÇÃO - Verificar cada aluno
for aluno in alunos:
    nome = aluno["nome"]
    nota = aluno["nota"]
    
    # CONDICIONAL - Verificar se passou
    if nota >= media_minima:
        situacao = "✅ APROVADO"
    else:
        situacao = "❌ REPROVADO"
    
    print(f"{nome}: {nota} - {situacao}")

# VARIÁVEL - Calcular média geral
notas = [aluno["nota"] for aluno in alunos]
media_geral = sum(notas) / len(notas)

print(f"\nMédia geral da turma: {media_geral:.2f}")

# CONDICIONAL - Verificar desempenho da turma
if media_geral >= 7:
    print("Turma teve bom desempenho! 🎉")
else:
    print("Turma precisa melhorar! 📚")