s = 0
for n in range (0, 6):
    n=int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print (f'O somatório dos numeros pares é {s}')