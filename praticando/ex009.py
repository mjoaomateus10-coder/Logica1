while True:

    print('\n1 - Ver saldo')
    print('2 - Sair')

    opcao = input('Escolha: ')

    if opcao == '1':
        print('Seu saldo é R$ 500')
    
    elif opcao == '2':
        print('Saindo...')
        break

    else:
        print('Opção inválida')