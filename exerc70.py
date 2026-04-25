continuar = 'S'
totalproduto = 0
produto1000 = 0
produtomaisbarato = float('inf')  
nomebarato = ''

while continuar == "S":
    print('='*30)
    print('SUPERMERCADO')
    print('='*30)
    
    nomeproduto = str(input('Digite o nome do produto: ')).strip().title()      
    valorproduto = float(input('Digite o valor do produto: R$ '))        
    
    totalproduto += valorproduto
    
    if valorproduto < produtomaisbarato:   
        produtomaisbarato = valorproduto   
        nomebarato = nomeproduto           
    
    if valorproduto >= 1000:
        produto1000 += 1
    
    print('='*30)
    continuar = str(input('Deseja cadastrar mais algum PRODUTO?[S/N]: ')).upper().strip()

print(f'Total da compra foi: R${totalproduto:.2f}')
print(f'Ao todo temos {produto1000} produtos acima de R$1000')
print(f'O produto mais barato foi {nomebarato} custando R${produtomaisbarato:.2f}')