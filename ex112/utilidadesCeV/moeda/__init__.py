def metade(preco=0, formatar=False):
    """
    -> Função que retorna a metade do preço de um produto.
    :param preco: Recebe o preço do produto.
    :param formatar: Define se o valor será formatado ou não.
    :return: Retorna a metade do valor recebido no parametro preço, formatado ou não.
    """
    return preco / 2 if not formatar else moeda(preco / 2)


def dobro(preco=0, formatar=False):
    """
    -> Função que retorna o dobro do preço de um produto.
    :param preco: Recebe o preço do produto.
    :param formatar: Define se o valor será formatado ou não.
    :return: Retorna a dobro do valor recebido no parametro preço, formatado ou não.
    """
    return preco * 2 if not formatar else moeda(preco * 2)


def aumentar(preco=0, aumento=0, formatar=False):
    """
    -> Função que acrescenta uma determinada taxa ao valor do produto.
    :param preco: Recebe o preço do produto.
    :param aumento: Recebe a taxa de aumento do preço do produto.
    :param formatar: Define se o valor será formatado ou não.
    :return: Retorna o preço do produto com acréscimo da taxa.
    """
    return preco + (preco * aumento / 100) if not formatar else moeda(preco + (preco * aumento / 100))


def diminuir (preco=0, desconto=0, formatar=False):
    """
    -> Função que decrementa uma determinada taxa ao valor do produto.
    :param preco: Recebe o preço do produto.
    :param desconto: Recebe a taxa de decremento do preço do produto.
    :param formatar: Define se o valor será formatado ou não.
    :return: Retorna o preço do produto com decremento da taxa.
    """
    return preco - (preco * desconto / 100) if not formatar else moeda(preco - (preco * desconto / 100))


def moeda(preco, moeda='R$'):
    """
    -> Função para formatar um determinado valor.
    :param preco: Recebe o preço do produto.
    :param moeda: Recebe a moeda do produto.
    :return: Retorna o preço do produto formatado.
    """
    return f"{moeda}{str(f'{preco:.2f}')}".replace('.', ',')


def resumo(preco=0, aumento=0, desconto=0):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f"{'Preço analisado:':<25}{moeda(preco)}")
    print(f"{'Dobro do preço:':<25}{dobro(preco,True)}")
    print(f"{'Metade do preço:':<25}{metade(preco,True)}")
    print(f"{f'{aumento}% de aumento:':<25}{aumentar(preco, aumento,True)}")
    print(f"{f'{desconto}% de redução:':<25}{diminuir(preco, desconto, True)}")
    print('-' * 40)
