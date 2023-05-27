"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import randint as sorteio
from time import sleep as aguarde

print("\n", "DESAFIO 88".center(43), "\n")
print('-' * 45)
print('JOGA NA MEGA SENA'.center(45))
print('-' * 45)

quantidade_jogos = int(input("Quantos jogos você quer que eu sorteie? "))  # Quantidade de jogos a sortear.
numeros_da_sorte = list()  # Cria uma lista para armazenar os números sorteados.
# jogos = list()  # Opcional
x = 0  # Contador para garantir que seja sorteado o número exato de jogos solicitado pelo usuário.

print(f"{f' SORTEANDO {quantidade_jogos} JOGOS ':-^45}")

while x < quantidade_jogos:
    contador = 0
    while contador < 6:
        numero = sorteio(0, 60)
        if numero not in numeros_da_sorte:
            numeros_da_sorte.append(numero)
            contador += 1
    x += 1
    print(f"Jogo {x}: {sorted(numeros_da_sorte)}")
    # jogos.append(numeros_da_sorte[:])
    numeros_da_sorte.clear()
    aguarde(1)

# for indice, jogo in enumerate(jogos):
#     print(f'jogo {indice + 1}: {jogo}')
#     aguarde(1)
    
print(f"{f' < BOA SORTE! > ':-^45}")
