from random import randint
numRobo = randint(1,10)
contador = 0
while True:
 print('-'*20)
 print('Vamos jogar Par ou Ímpar')
 print('-'*20)
 PouI=str(input('Escolha Par ou Ímpar [P/I]: ')).upper()
 numPessoa=int(input('Escolha um número: '))
 soma = numPessoa + numRobo
 if PouI == 'P':
   if soma % 2 == 0:
     print (f'(Número da máquina) {numRobo} + {numPessoa} (Seu número) é par, Você ganhou!!!')
     contador += 1
   else: 
     print (f'(Número da máquina) {numRobo} + {numPessoa} (Seu número) é impar, Você perdeu!')
     break
 elif PouI == 'I':
   if soma % 2 != 0:
     print (f'(Número da máquina) {numRobo} + {numPessoa} (Seu número) é impar, Você ganhou!!!')
     contador += 1
   else: 
     print (f'(Número da máquina) {numRobo} + {numPessoa} (Seu número) é par, Você perdeu!')
     break
 else:print('Escolha entre P OU I')
print(f'Você ganhou {contador} vezes')
  
  
 
