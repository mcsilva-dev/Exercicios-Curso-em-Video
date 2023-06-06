"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.

ex:
escreva('Olá, Mundo!')

saida:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~"""

print("\n", f"{'DESAFIO 97'.center(38)}", "\n")


def escreva(texto, string='~'):
    tamanho = len(texto) + 4
    print(string * tamanho)
    print(f'{texto}'.center(tamanho))
    print(string * tamanho)


escreva('Gustavo Guanabara', '*')
escreva('Curso de Python no Youtube', '=')
escreva('CeV')
