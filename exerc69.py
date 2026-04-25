continuar = 'S'
sexoM = maioresde18 = mulher20 = 0

while continuar == "S":
    print('='*30)
    print('CADASTRO DE PESSOAS')
    print('='*30)
    
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        maioresde18 += 1
    
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if sexo == "M":
        sexoM += 1
    if sexo == "F" and idade <= 20:
        mulher20 += 1
    
    print('='*30)
    continuar = str(input('Deseja cadastrar mais alguém?[S/N]: ')).upper().strip()

print(f'Total de pessoas acima dos 18 anos: {maioresde18}') 
print(f'Ao todo temos {sexoM} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')