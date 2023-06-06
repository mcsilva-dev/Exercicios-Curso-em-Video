"""Faça um programa que tenha uma função chamada contador(), que receba 3 parâmetros: inicio, fim e passo e realize a
contagem. Seu programa tem que realizar 3 contagens através da função criada:
A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada."""

from time import sleep

print("\n", f"{'DESAFIO 98'.center(38)}", "\n")


def contador(inicio, fim, passo=1):
    print('-' * 40)
    salto = passo if passo > 0 else 1
    print(f"Contagem de {inicio} até {fim} de {salto} em {salto}")
    sleep(1)
    if fim > inicio:
        for x in range(inicio, fim + 1, salto):
            print(x, end=' ')
            sleep(0.5)
    else:
        for x in range(inicio, fim - 1, -salto):
            print(x, end=' ')
            sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-' * 40)
print("Agora é sua vez de personalizar a contagem!")
i = int(input("INICIO: ".ljust(8)))
f = int(input("FIM: ".ljust(8)))
p = abs(int(input('PASSO: '.ljust(8))))

contador(i, f, p)
