resp = 'S'
soma = quant = media = maior = menor = 0
while resp == 'S':
    num=int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp=str(input('Quer continuar [S/N]?\n->')).upper().strip()
print(f'Você digitou {quant} números e a média foi {soma/quant}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')