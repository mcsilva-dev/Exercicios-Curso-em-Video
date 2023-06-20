"""Faça um programa que tenha uma função chamada ficha(), qye receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

print('\n', 'DESAFIO 103'.center(38), '\n')
print('-' * 40)


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome_jogador = input('Nome do jogador: ').strip()
numero_gols = input('Número de gols: ').strip()
numero_gols = int(numero_gols) if numero_gols.isnumeric() else 0

if nome_jogador == '':
    ficha(gols=numero_gols)
else:
    ficha(nome_jogador, numero_gols)
