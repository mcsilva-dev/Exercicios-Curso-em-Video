# Faça um progrma que leia o comprimento do cateto adjacente de um triangulo retângulo, calcule e
# mostre o comprimento da hipotenusa.

from math import hypot

print('\n      ====== DESAFIO 17 ======      ')

co = float(input('\nComprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print(f'A hipotenusa é {hypot(co, ca):.2f}')

# Forma de realizar sem importar nenhuma biblioteca ou ferramenta
"""print(f'A hipotenusa é {(co ** 2 + ca ** 2) ** (1/2):.2f}')"""
