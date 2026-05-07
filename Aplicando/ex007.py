# Praticando
'''
Festa de 18 anos.

'''

# Guardando a idade que a pessoa digitar
seguranca = int(input('Poderia dizer a sua idade? '))

idade_minima = 16
idade_maior = 18

if seguranca >= idade_maior:
    print('Pode entrar, maior de idade liberado!')
elif seguranca >= idade_minima:
    print('Pode entrar, porém com autorização.')
else:
    print('Acesso negado. Muito jovem.')