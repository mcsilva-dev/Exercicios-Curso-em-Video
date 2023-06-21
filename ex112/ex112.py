"""Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função input(), mas com validação de dados para aceitar apenas
valores que sejam monetários."""

from utilidadesCeV import dado, moeda

print("\n", "DESAFIO 112".center(38), "\n")

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)


