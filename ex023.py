# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex:
# Digite um número: 1834
#
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

print(f'\n{"====== DESAFIO 24 ======":^37}')

# print('\nMinha solução:')
num = input('\nDigite um número (0/9999): ').strip().zfill(4)
sep = ' '.join(num).split()

print(f'\nUnidade: {sep[3]}')
print(f'Dezena: {sep[2]}')
print(f'Centena: {sep[1]}')
print(f'Milhar: {sep[0]}')

# print('\nSolução do professor')

# num = int(input('Digite um número: '))
# n = str(num).zfill(4)
# print(f'\n Unidade: {n[3]}')
# print(f'Dezena: {n[2]}')
# print(f'Centena: {n[1]}')
# print(f'Milhar: {n[0]}')

# Podemos fazer também da seguinte forma:
# > Unidade = num // 1 % 10
# > Dezena = num // 10 % 10
# > Centena = num // 100 % 10
# > Milhar = num // 1000 % 10
