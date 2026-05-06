# Desafio do Radar Eletrônico
velocidade = float(input('Qual a velocidade atual do carro em km/h? '))

if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido de 80km/h.')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
else:
    print('Tenha um bom dia! Dirija com segurança.')