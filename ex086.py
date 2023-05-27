"""Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valores lidos pelo teclado.
No final mostre a matriz na tela, com a formatação correta."""

print("\n", "DESAFIO 86".center(38), "\n")

matriz = [[], [], []]  # Cria uma lista com 3 listas.
for x in range(0, 3):  # Cria um laço que conta as linhas da matriz.
    for y in range(0, 3):  # Cria um laço para as colunas da matriz.
        matriz[x].append(int(input(f"Digite o valor para [{x}, {y}]: ")))  # Recebe um valor do usuário.

print('-' * 40)

# Exibe o resultado da matriz.
for x in range(0, 3):
    for y in range(0, 3):
        print(f"[{matriz[x][y]:^8}] ", end="" if y < 2 else "\n")
