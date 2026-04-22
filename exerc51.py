p=int(input('DIGITE O PRIMEIRO TERMO: '))
r=int(input('DIGITE A RAZÃO: '))
decimo = p+(10-1)*r
for c in range (p, decimo+r, r):
    print( c, end=' -> ' )