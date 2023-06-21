"""Crie um módulo chamdo moeda.py que tenha funções incorporadas aumentar(), diminuir(), dobro() e metada().
Faça também um programa que importe esse módulo e use algumas dessas funções."""

from ex112.utilidadesCeV import moeda

print("\n", "DESAFIO 107".center(38), "\n")

p = float(input("Digite o preço: R$"))

print(f"A metade de {p} é {moeda.metade(p)}")
print(f"O dobro de {p} é {moeda.dobro(p)}")
print(f"Aumento 10%, temos {moeda.aumentar(p, 10)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(p, 13)}")
