s = 0
s2 = 0
for c in range (0, 7):
    nasc=int(input('Digite seu ano nascimento: '))
    if 2026 - nasc >= 18:
        s += 1
    else: s2 += 1
print(f'A quantidade de pessoas maiores de idade é {s} e de menores é {s2}')
