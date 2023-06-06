"""Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somapar(). A primeira
função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
valores PARES sorteados pela função anterior."""

from random import randint
from time import sleep

print("\n", f"{'DESAFIO 100'.center(38)}", "\n")


def somapar(l):
    return sum([v for v in l if v % 2 == 0])


def sorteia():
    lista = list(randint(1, 10) for c in range(0, 5))
    print('Sorteando 5 valores da lista: ', end="")
    for x in lista:
        print(x, end=" ")
        sleep(0.5)
    print('PRONTO!')
    print(f"Somando os valores pares de {lista}, temos {somapar(lista)}")


sorteia()
