# Crie um programa que faça o computador jogar jokenpô com você.

from random import choice
from time import sleep

cores = {
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'limpa': '\033[m'
}

print(f"\n{'====== DESAFIO 45 ======':^60}\n")
print(f"{'JOKENPÔ':^60}\n")

player = int(input(f"""FAÇA SUA ESCOLHA:
1. Pedra
2. Papel
3. Tesoura
Sua escolha: """))
escolha = 'Pedra', 'Papel', 'Tesoura'
player_escolha = {
    1: 'Pedra',
    2: 'Papel',
    3: 'Tesoura'
}
maquina = choice(escolha)
print(f"Você escolheu {cores['verde']}{player_escolha[player]}{cores['limpa']} "
      f"e a maquina escolheu {cores['vermelho']}{maquina}{cores['limpa']}.")
print("RESULTADO:")
sleep(3)
if player_escolha[player] == maquina:
    print(f'{cores["verde"]}EMPATE{cores["limpa"]}')
elif player_escolha[player] == 'Pedra' and maquina == 'Tesoura':
    print(f'{cores["verde"]}Você ganhou! Pedra quebra Tesoura.')
elif player_escolha[player] == 'Tesoura' and maquina == 'Pedra':
    print(f'{cores["vermelho"]}A Maquina venceu! Pedra quebra Tesoura.')
elif player_escolha[player] == 'Papel' and maquina == 'Tesoura':
    print(f'{cores["vermelho"]}A Maquina venceu! Tesoura corta Papel.')
elif player_escolha[player] == 'Tesoura' and maquina == 'Papel':
    print(f'{cores["verde"]}Você ganhou! Tesoura corta Papel.')
elif player_escolha[player] == 'Papel' and maquina == 'Pedra':
    print(f'{cores["verde"]}Você ganhou! Papel embrulha Pedra.')
elif player_escolha[player] == 'Pedra' and maquina == 'Papel':
    print(f'{cores["vermelho"]}A Maquina venceu! Papel embrulha Pedra.')
