"""Faça um programa que tenha uma função chamada area(), que recebe as dimensões de um terreno retangular
(largura e comprimento) e mostre a area do terreno."""

print("\n", f"{'DESAFIO 96'.center(38)}", "\n")


def area(largura, comprimento):
    return largura * comprimento


print(f"{'Controle de Terrenos'.center(40)}")
print('-' * 40)


l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))

print(f"A área de um terreno de {l}x{c} é de {area(l, c):.1f}m².")
