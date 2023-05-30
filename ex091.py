"""Crie um programa onde 4 pontuacao_jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem. Sabendo que o vencedor tirou o maior número no dado."""

from random import randint as dado
from time import sleep as aguarde

print("\n", f'{"DESAFIO 91":^38}', '\n')

# Primeiro cria o dicionário randomico.
pontuacao_jogadores = {'Jogador1': dado(1, 6),
                       'Jogador2': dado(1, 6),
                       'Jogador3': dado(1, 6),
                       'Jogador4': dado(1, 6)}
# Necessário criar um dicionário diferente para o ranking_jogadores.
ranking_jogadores = dict()
# Utilizar uma lista para armazenar os valores de cada chave do dicionario pontuacao_jogadores.
lista_valores = list()
x = 0

# Cria um laço para armazenar os valores na lista de valores.
for valores in pontuacao_jogadores.values():
    lista_valores.append(valores)

# Após isso organizo de forma decrescente os valores dentro da lista.
lista_valores.sort(reverse=True)

# Neste looping a ideia é, pegar cada valor da lista de valores e encontrar o jogador dentro do primeiro dicionário que
# tem o mesmo valor e adicionar ao dicionário ranking na ordem correta.
while len(ranking_jogadores) < len(pontuacao_jogadores):
    for valor in lista_valores:
        for jogador, dado in pontuacao_jogadores.items():
            if valor == dado:
                ranking_jogadores[jogador] = dado

print("Valores sorteados:")

for key, valor in pontuacao_jogadores.items():
    print(f"\tO {key} tirou {valor}")
    aguarde(1)

print('Ranking dos jogadores:')

for key, valor in ranking_jogadores.items():
    x += 1
    print(f'\t{x}º lugar: {key} com {valor}')
    aguarde(1)
