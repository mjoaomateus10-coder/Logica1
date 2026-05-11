# ========================================
# EXERCÍCIO 4 - CALCULAR MÉDIA E CONCEITO
# ========================================
print("=" * 50)
print("EXERCÍCIO 3 - NOTAS DE 5 ALUNOS")
print("=" * 50)

alunos = {
    "Ana": [8.5, 9.0, 8.5],
    "Bruno": [6.0, 5.5, 6.5],
    "Carlos": [9.5, 9.0, 9.5],
    "Diana": [7.0, 7.5, 7.0],
    "Edu": [4.5, 5.0, 4.8]
}

print("RESULTADO FINAL DOS ALUNOS:\n")

for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    
    if media >= 9:
        conceito = "Excelente"
    elif media >= 8:
        conceito = "Muito Bom"
    elif media >= 7:
        conceito = "Bom"
    elif media >= 6:
        conceito = "Satisfatório"
    else:
        conceito = "Insuficiente"
    
    status = "✓ APROVADO" if media >= 7 else "✗ REPROVADO"
    
    print(f"{aluno}:")
    print(f"  Notas: {notas}")
    print(f"  Média: {media:.2f}")
    print(f"  Conceito: {conceito}")
    print(f"  {status}\n")

print()