# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, tan, sin, radians

print('\n      ====== DESAFIO 18 ======      ')

angulo = radians(int(input('\nDigite um angulo qualquer: ')))

print(f'O seno é {sin(angulo):.4f}.')
print(f'O cosseno é {cos(angulo):.4f}.')
print(f'A tangente é {tan(angulo):.4f}.')
