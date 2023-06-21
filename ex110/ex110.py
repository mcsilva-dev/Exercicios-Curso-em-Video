"""Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
informações geradas pelas funções que ja temos no módulo criado até aqui."""

from ex112.utilidadesCeV import moeda

print("\n", "DESAFIO 110".center(38), "\n")

p = float(input("Digite o preço: R$"))
moeda.resumo(p, 10, 35)
