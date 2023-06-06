"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

from time import sleep

print("\n", f"{'DESAFIO 99'.center(38)}", "\n")


def maior(*n):
    print('-' * 40)
    print('Analisando os valores passados...')
    sleep(1)
    # m = 0
    for v in n:
        print(v, end=' ')
        # if v > m:
        #     m = v
        sleep(0.5)
    print(f'Foram informados {len(n)} valores ao todo.')
    sleep(0.5)
    print(f"O maior valor informado foi {max([v for v in n]) if len(n) > 0 else 0}")
    sleep(0.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
