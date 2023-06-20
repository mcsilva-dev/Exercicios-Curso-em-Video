"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo
de cálculo fatorial."""

print('\n', 'DESAFIO 102'.center(38), '\n')
print('-' * 40)


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a operação.
    :return: O valor do Fatorial de um número n
    """
    fat = 1
    for x in range(n, 0, -1):
        fat *= x
        if show and x > 1:
            print(f"{x}", end=' x ')
        elif show and x == 1:
            print(f"{x}", end=' = ')
    return fat


print(fatorial(6, True))
help(fatorial)
