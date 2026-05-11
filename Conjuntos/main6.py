# ========================================
# EXERCÍCIO 6 - CONTAGEM E ESTATÍSTICAS
# ========================================
print("=" * 50)
print("EXERCÍCIO 5 - ANÁLISE DE TEMPERATURAS")
print("=" * 50)

temperaturas = [22, 25, 28, 30, 26, 24, 29, 31, 27, 23, 25, 28]
quentes = 0
agradaveis = 0
frias = 0
temperaturas_altas = []
temperaturas_baixas = []

print(f"Temperaturas do mês: {temperaturas}\n")

for temp in temperaturas:
    if temp > 28:
        quentes += 1
        temperaturas_altas.append(temp)
    elif temp >= 20 and temp <= 28:
        agradaveis += 1
    else:
        frias += 1
        temperaturas_baixas.append(temp)

media_temp = sum(temperaturas) / len(temperaturas)
temp_maxima = max(temperaturas)
temp_minima = min(temperaturas)

print("ESTATÍSTICAS:")
print(f"Temperatura média: {media_temp:.1f}°C")
print(f"Temperatura máxima: {temp_maxima}°C")
print(f"Temperatura mínima: {temp_minima}°C\n")

print("CLASSIFICAÇÃO:")
print(f"Dias quentes (> 28°C): {quentes} dias")
print(f"Dias agradáveis (20-28°C): {agradaveis} dias")
print(f"Dias frios (< 20°C): {frias} dias\n")

print(f"Dias com temperatura alta: {temperaturas_altas}")
print(f"Dias com temperatura baixa: {temperaturas_baixas}\n")

if media_temp > 26:
    print("🔥 Mês foi QUENTE")
elif media_temp >= 20:
    print("⛅ Mês foi AGRADÁVEL")
else:
    print("❄️ Mês foi FRIO")

print("\n" + "=" * 50)
print("✓ TODOS OS 5 EXERCÍCIOS EXECUTADOS COM SUCESSO!")
print("=" * 50)