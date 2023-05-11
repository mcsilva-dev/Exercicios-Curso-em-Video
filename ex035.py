# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triangulo.

from colorise import fprint

print(f"\n{'====== DESAFIO 35 ======':^37}\n")


l1 = int(input('Digite o valor da 1° reta: '))
l2 = int(input('Digite o valor da 2° reta: '))
l3 = int(input('Digite o valor da 3° reta: '))

if not(not l1 < l2 + l3 or not l2 < l1 + l3 or not l3 < l2 + l1):
    fprint('{bold,fg=green}É POSSÍVEL {reset}formar um triângulo.')
else:
    fprint('{bold,fg=red}NÃO É POSSÍVEL{reset} formar um triângulo.')
