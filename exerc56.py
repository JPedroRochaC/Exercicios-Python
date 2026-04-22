somaidade=0
nvelho=''
tmulher20=0
mediaidade=0
maioridH=0
for p in range (1, 5):
   nome=str(input(f'Digite o nome da {p}° pessoa: '))
   idade=int(input('Digite a idade: '))
   sexo=str(input('Digite o sexo [M/F]: ')).upper().strip()
   somaidade += idade
   if p == 1 and sexo == 'M':
      maioridH = idade
      nvelho = nome
   if sexo == 'M' and idade > maioridH:
      maioridH = idade
      nvelho = nome
   if sexo == 'F' and idade < 20:
      tmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idades é {mediaidade}')
print(f'O homem mais velho tem {maioridH} anos e se chama {nvelho}')
print(f'Ao todo são {tmulher20} mulheres com menos de 20 anos')