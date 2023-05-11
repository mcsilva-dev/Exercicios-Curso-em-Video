#  Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.

from math import trunc

print('\n      ====== DESAFIO 16 ======      ')
num = float(input('\nDigite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}')

""" Outras soluções sem importar bibliotecas:
print(f'O número {num} tem a parte inteira {int(num)}')
ou 
print(f'O número {num} tem a parte inteira {num:.0f}')
"""
