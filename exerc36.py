print('--EMPRESTIMOS--')
valor = float(input('Qual valor da casa?\n ==> '))
sala = float(input('Qual seu salário?\n ==> '))
anos = int(input('Em quantos anos você pretende pagar?\n ==> '))

trinta = sala * 0.30 
prestação = valor / (anos*12)
print (f'A prestação mensal fica R${prestação:.2f} em {anos*12}x')

if prestação <= trinta :
    print('Empréstimo feito com sucesso!')
else:
    print('Empréstimo negado! A prestação excede 30% do seu salário!')