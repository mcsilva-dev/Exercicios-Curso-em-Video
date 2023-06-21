def leiaDinheiro(text):
    """
    -> Função validadora que funciona de forma parecida ao input, porém garantindo tratamento de possíveis erros.
    :param text: Recebe o texto que deseja apresentar no input.
    :return: Retorna o valor de n como Float.
    """
    while True:
        n = input(text).strip().replace(",", ".")
        try:
            return float(n)
        except ValueError:
            print(f"\033[1;31mERRO: '{n}' é um preço invalido!\033[m")
