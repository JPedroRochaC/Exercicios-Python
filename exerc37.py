from decimal import Decimal
print('--CONVERTER N° INTEIRO--')
n=int(input('Digite um número inteiro\n ==> '))
conversão=int(input('Você quer converter ele para ' \
'\n 1.BINÁRIO\n 2.OCTAL\n 3.HEXADECIMAL\n ==> '))

if conversão == 1:
    print(f'O número {n} convertido para binário fica {bin(n)[2:]}')
elif conversão == 2:
    print(f'O número {n} convertido para octal fica {oct(n)[2:]}')
elif conversão == 3:
    print(f'O número {n} convertido para hexadecimal fica {hex(n)[2:]}')
else :
 print('Opcão invalida')