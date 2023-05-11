# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.
# Ex: Ana Maria de Souza
# > Primeiro = Ana
# > Ultimo = Souza

print(f'\n{"====== DESAFIO 27 ======":^37}')

nome = input('\nDigite seu nome completo: ').title().strip()
snome = nome.split()

print(f'O primeiro nome = {snome[0]}')
print(f'O ultimo nome = {snome[len(snome) - 1]}')
