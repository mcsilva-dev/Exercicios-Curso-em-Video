"""Modifique as funções do que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se
o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""

from ex112.utilidadesCeV import moeda

print("\n", "DESAFIO 109".center(38), "\n")

p = float(input("Digite o preço: R$"))

print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}")
print(f"Aumento 10%, temos {moeda.aumentar(p, 10, True)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}")
