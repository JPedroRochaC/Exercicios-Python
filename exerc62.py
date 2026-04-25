n=int(input('Digite um número [0 para parar]: '))
s = n
contador = 1
while n != 0:
    n=int(input('Digite um número [0 para parar]: '))
    s += n
    if n != 0:
     contador += 1
print(f'Você digitou {contador} e a soma entre eles foi {s}')