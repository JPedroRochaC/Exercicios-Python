import random
numero = random.randint(1, 10)
chute=int(input('Tente acertar um número de 1 até 10\n->'))
contador = 1
while chute != numero:
    print('Errou')
    chute=int(input('Tente novamente acertar um número de 1 até 10\n->'))
    contador += 1
print(f'Parabéns, você acertouu!!!\ncom {contador} tentativas')