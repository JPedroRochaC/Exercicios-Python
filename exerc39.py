print('--ALISTAMENTO--')
nasc=int(input('DIGITE O ANO DO SEU NASCIMENTO\n ==>'))
idade = 2026 - nasc
if idade == 18:
    print('Você tem 18 anos, você deve se alistar imediamente')
elif idade < 18:
    print(f'Você tem {idade} anos e deve se alistar em {18-idade} anos')
else:
    print(f'Você tem {idade} e deveria ter se alistado a {idade-18} anos')