while True:
    print('-'*30)
    print('BEM VINDO AO BANCO PR')
    print('-'*30)
    
    valor = float(input('Digite o valor que você deseja sacar: '))
    
    cedulas50 = int(valor // 50)
    resto = valor % 50     
    cedulas10 = int(resto // 10)
    resto = resto % 10       

    cedulas1 = int(resto // 1)

    print(f'Cédulas de R$50: {cedulas50}')
    print(f'Cédulas de R$10: {cedulas10}')
    print(f'Cédulas de R$1:  {cedulas1}')

    continuar = input('Deseja fazer outro saque? [S/N]: ').upper().strip()
    if continuar != 'S':
        break