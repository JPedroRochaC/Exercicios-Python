print('--PINTOR--')
l=float(input('Digite a largura da parede: '))
a=float(input('Digite a altura da parede: '))
ar = l*a
t = ar/2
print(10*'--')
print(f'Sua parede tem a dimensão de {l}x{a} e a sua área é de {ar:.2f}')
print(f'Para pintar essa parede, você precisará de {t:.2f}L de tinta')