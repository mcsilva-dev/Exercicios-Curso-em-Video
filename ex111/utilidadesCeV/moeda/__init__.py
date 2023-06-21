def metade(preco, formatar=False):
    return preco / 2 if not formatar else moeda(preco / 2)


def dobro(preco, formatar=False):
    return preco * 2 if not format else moeda(preco * 2)


def aumentar(preco, aumento=10, formatar=False):
    return preco + (preco * aumento / 100) if not formatar else moeda(preco + (preco * aumento / 100))


def diminuir(preco, desconto=10, formatar=False):
    return preco - (preco * desconto / 100) if not formatar else moeda(preco - (preco * desconto / 100))


def moeda(preco):
    return f"R${str(preco).replace('.', ',')}"


def resumo(preco, aumenta, diminui):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f"Preço analisado:{moeda(preco):>20}")
    print(f"Dobro do preço: {dobro(preco,True):>20}")
    print(f"Metade do preço:{metade(preco,True):>20}")
    print(f"{aumenta}% de aumento: {aumentar(preco,aumenta,True):>20}")
    print(f"{diminui}% de redução: {diminuir(preco, diminui, True):>20}")
    print('-' * 40)
