n = int(input('Digite um número pra saber o fatorial dele: '))
m = 1 
if n == 0:
    print(1)
else:
    while n >= 1:
        m = m * n
        n -= 1
    print(m)