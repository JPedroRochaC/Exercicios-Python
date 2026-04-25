n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
operacao = 0
while operacao != 5:
 print('--------------------------------------')
 operacao=int(input('Qual operação você deseja fazer?\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR VALOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA\n--> '))
 if operacao == 1:
  print(f'A soma do número {n1} + {n2} é igual a {n1+n2}')
 if operacao == 2:
  print(f'A multiplicação do número {n1} x {n2} é igual a {n1*n2}')
 if operacao == 3:
  if n2 > n1: 
   print(f'O maior valor é {n2}')
  elif n1> n2:
   print(f'O maior valor é {n1}')
  else: print('Os valores são iguais')
 if operacao == 4:
  print('--------------------------------------')
  n1=int(input('Digite um novo valor: '))
  n2=int(input('Digite mais um valor: '))
print('--------------------------------------')
print('Até mais, Obrigado!')


  