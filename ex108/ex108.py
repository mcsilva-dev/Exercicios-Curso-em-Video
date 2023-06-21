"""Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como
um valor monetário formatado."""

from ex112.utilidadesCeV import moeda

print("\n", "DESAFIO 108".center(38), "\n")

p = float(input("Digite o preço: R$").replace(',', '.'))

print(f"A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"Aumento 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}")
print(f"Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}")
