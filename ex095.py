"""Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
de aproveitamento de cada jogador."""

print("\n", f"{'DESAFIO 95':^48}", "\n")

estatísticas_jogadores = list()

while True:
    print("-" * 50)
    jogador = {'Nome': str(input("Nome do Jogador: ")),
               'Gols': [],
               'Total': 0
               }
    partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    for partida in range(0, partidas):
        jogador['Gols'].append(int(input(f"Quantos gols na partida {partida}? ")))
    jogador['Total'] = sum(jogador['Gols'])
    estatísticas_jogadores.append(jogador.copy())
    while True:
        question = input("Quer continuar? [S/N] ").strip().upper()[0]
        if question in 'SN':
            break
        else:
            print("Tente novamente.", end=" ")
    if question == 'N':
        print("-=" * 25)
        break

print(f'{"cod":<6}{"Nome":<15}{"Gols":<15}{"Total":<15}')
print("-" * 50)

for cod in range(0, len(estatísticas_jogadores)):
    print(f"{cod:<6}", end='')
    for chaves, valor in estatísticas_jogadores[cod].items():
        print(f"{str(valor):<15}", end="")
    print()

print("-" * 50)

while True:
    while True:
        indice = int(input("Mostrar dados de qual jogador? "))
        if 0 <= indice < len(estatísticas_jogadores) or indice == 999:
            break
        else:
            print(f"ERRO! Não existe jogador com código {indice}! Tente novamente")
            print("-" * 50)
    if indice == 999:
        print("<< VOLTE SEMPRE >>")
        break
    print(f"--  LEVANTAMENTO DO JOGADOR {estatísticas_jogadores[indice]['Nome']}:")
    for partida in range(0, len(estatísticas_jogadores[indice]['Gols'])):
        print(f"\tNo jogo {partida} fez {estatísticas_jogadores[indice]['Gols'][partida]} gols.")
    print("-" * 50)
