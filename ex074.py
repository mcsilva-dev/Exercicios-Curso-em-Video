"""Crie um programa que vai gerar cinco números alestorios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

print("\n", "DESAFIO 74".center(60), "\n")

from random import randint

aleatorios = []

while len(aleatorios) < 5:
    random = randint(1, 10)
    aleatorios.append(random) if random not in aleatorios else aleatorios

numeros = tuple(aleatorios)

print(f"{'NÚMEROS ALEATÓRIOS GERADOS':-^50}")

for numero in numeros:
    print(f"{numero:8}", end=" ")

print()
print('-' * 50)
print(f"O maior valor é {max(numeros)}.")
print(f"O menor valor é {min(numeros)}.")
print(f"Os numeros em ordem são: ", end='')

for numero in sorted(aleatorios):
    print(f"{numero}", end=" ")
print()
