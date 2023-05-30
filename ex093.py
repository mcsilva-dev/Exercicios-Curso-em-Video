"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feito durante o campeonato."""

print("\n", f"{'DESAFIO 93':^58}", "\n")

estasticas_jogador = dict()
gols_por_partida = list()
estasticas_jogador['Nome'] = str(input("Nome do Jogador: "))
numero_partidas = int(input(f"Quantas partidas {estasticas_jogador['Nome']} jogou? "))

for partida in range(0, numero_partidas):
    gols = int(input(f"Quantos gols na partida {partida}? "))
    gols_por_partida.append(gols)

estasticas_jogador['Gols'] = gols_por_partida[:]
estasticas_jogador['Total'] = sum(gols_por_partida)

print('-' * 60)
print(estasticas_jogador)
print('-' * 60)

for chave, valor in estasticas_jogador.items():
    print(f"O campo {chave} tem o valor {valor}.")

print('-' * 60)
print(f"O jogador {estasticas_jogador['Nome']} jogou {numero_partidas}.")

for partida in range(0, numero_partidas):
    print(f'\t=> Na partida {partida}, fez {estasticas_jogador["Gols"][partida]} gols.')

print(f'Foi um total de {estasticas_jogador["Total"]} gols.')
