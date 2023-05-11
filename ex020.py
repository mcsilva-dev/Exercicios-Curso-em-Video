# O mesmo professo do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quartro alunos e mostre a ordem sorteada.

from random import shuffle, sample

print('\n      ====== DESAFIO 20 ======      ')

a1 = input('\nNome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')

# Outra forma de fazer por meio de embaralhamento:
# lista = f'{a1} {a2} {a3} {a4}'.split()
# shuffle(lista)

print(f'\nA ordem sorteado de apresentação dos alunos é = {sample([a1, a2, a3, a4], k=4)}')
