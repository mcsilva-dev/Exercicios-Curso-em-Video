"""Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número
já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente."""

print("\n", "DESAFIO 79".center(50), "\n")

lista = []

while True:
    numero = int(input("Digite um valor: "))  # Recebe do usuário um número inteiro.
    if numero not in lista:  # Se o número não estiver na lista, é executado o bloco a seguir.
        lista.append(numero)  # Adiciona o elemento a lista.
        print("Valor adicionado com sucesso...")  # Informa ao usuário que o valor foi adicionado.
    else:  # Se o valor já existe na lista é informado que o valor é duplicado e que não será adicionado.
        print("Valor duplicado! Não vou adicionar...")
    while True:  # Cria um looping infinito, com intuito de garantir que o usuário corresponda corretamente.
        resposta = input("Quer continuar? [S/N] ").upper().strip()[0]  # Recebe a resposta do usuário.
        if resposta in 'SN':  # Caso a primera letra seja S ou N é interrompido o looping.
            break
        else:  # Caso contrário é solicitado ao usuário que tente novamente.
            print("Tente novamente.", end=" ")
    if resposta == 'N':  # Se a resposta do usuário foi N, o looping principal é parado
        print('-' * 50)
        lista.sort()  # organiza a lista de forma crescente.
        break

print(f"Você digitou os valores {lista}")  # No fim é exibida a lista para o usuário.
