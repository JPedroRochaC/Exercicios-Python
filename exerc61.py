p=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão da PA: '))
contador =1
termo = p
total = 0
mais = 10
while mais != 0:
 total = total + mais
 while contador <= total :
    print(termo, end=' -> ')
    contador += 1
    termo += r
 print('PAUSA')
 mais=int(input('Quantos números você quer mostrar a mais? '))
print('Fim da PA')
print(f'Sua PA tem {contador} termos')