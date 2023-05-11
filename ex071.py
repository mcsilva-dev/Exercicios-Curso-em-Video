"""Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuário qual será o valor
sacado (número inteiro) e o programa vai informar quantas cédulas de valor será entregues. O
BS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print("\n", "DESAFIO 71".center(47), "\n")
print("BANCO SILVA".center(50))
print("-" * 50)
valor = int(input("Informe o valor a sacar (Apenas inteiro): R$"))  # Recebe o valor que o usuário deseja sacar.
apagar = valor  # Adiciona a uma nova variavel o valor a ser sacado para que possa ser decrementado.
cedula = 50  # Inicia as cédulas pela cédula mais alta disponivel no caixa.
quantidade_cedulas = 0  # Acumula a quantidade de determinada celula foi sacada.
print("-" * 50)
while True:
    if cedula <= apagar:  # Verifica se o valor da cédula cedula é menor ou igual ao valor a pagar para o usuário.
        apagar -= cedula  # Decrementa o valor cedula da cedula do valor a pagar.
        quantidade_cedulas += 1  # Adiciona 1 no acumulador de cédulas.
    else:  # Caso a cédula seja maior que o valor ao pagar ao usuário, o bloco a seguir será executado.
        if quantidade_cedulas > 0:  # Se o número de cédulas for maior que zero,
            # irá exibir o número de cédulas daquele valor foi sacada.
            print(f"{quantidade_cedulas} cédula(s) de R${cedula:.2f}")
            quantidade_cedulas = 0  # Após exibir cédulas recebe o valor de 0 novamente.
        if apagar == 0:  # Se não restar valor a pagar o laço é interrompido.
            break
        if cedula == 50:  # Checa o valor cedula e substitui pelo da proxima cédula de valor mais baixo.
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
print("-" * 50)
print("Volte sempre ao BANCO SILVA! Tenha um bom dia!")
