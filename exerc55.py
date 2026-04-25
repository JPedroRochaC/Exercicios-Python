maiorpeso = 0
for c in range (1, 6):
    peso=float(input(f'Digite o peso da {c}° pessoa '))
    if peso > maiorpeso:
      maiorpeso = peso
print(f'O maior peso : {maiorpeso}kg')