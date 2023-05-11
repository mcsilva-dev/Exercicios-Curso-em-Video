# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

print('\n      ====== DESAFIO 11 ======')

largura = float(input('\nLargura da parede (m): '))
altura = float(input('Altura da parede (m): '))
area = largura * altura
tinta = area / 2

print(f'Sua parede tem a dimensão de {largura} x {altura} e sua área é de {area}m².')
print('Sabendo que cada litro de tinta pinta 2m²,')
if tinta < 2:
    print(f'para pintar essa parede, será necessário {tinta}l de tinta.')
else:
    print(f'para pintar essa parede, serão necessários {tinta}l de tinta.')
