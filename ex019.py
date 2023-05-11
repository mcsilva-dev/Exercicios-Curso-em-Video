# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

print('\n      ====== DESAFIO 19 ======      ')

a1 = input('\nNome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')

print(f'\nO aluno sorteado para apagar o quadro foi {choice([a1, a2, a3, a4])}')
