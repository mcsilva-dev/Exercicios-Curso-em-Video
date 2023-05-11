"""Crie um programa que leia dois valores e mostre um menu na tela:

[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep

print("\n", "DESAFIO 59".center(30), "\n")
print("REALIZANDO OPERAÇÕES".center(30), "\n")

n1 = int(input("Primeiro valor: "))  # Recebe o primero valor do digitado pelo usuário.
n2 = int(input("Segundo valor: "))  # Recebe o segundo valor digitado pelo usuário.

print("-=-" * 10)

while True:  # Entrando em um loop até que seja interrompido pelo flag digitado pelo usuário.
    print("MENU DE OPÇÕES:"  # Será apresentado ao usuário um menu de opções, 
          # para que o mesmo possa selecionar de acordo com sua necessidade.
          "\n[1] - Soma"
          "\n[2] - Mulplicação"
          "\n[3] - Maior"
          "\n[4] - Novos números"
          "\n[5] - Sair do programa")
    while True:  # Este loop serve para garantir que a opção digitada pelo usuário,
        # seja uma opção valida e não aceite nenhuma outra.
        opcao = int(input(f"Sua opção: "))  # Recebe a opçãpoo selecionada pelo usuário.
        if 0 < opcao <= 5:  # Caso a opção esteja dentro das opções validas, o looping será interrompido.
            break
        else:  # Senão o usuario irá receber uma mensagem informado que o valor digitado é invalido e
            # solicitado que digite um novo valor.
            print("Opção inválida! Digite novamente.")
    if opcao == 1:  # Caso o usuário opte pela soma, utilizando a opção 1, este bloco será executado.
        soma = n1 + n2
        print(f"{n1} + {n2} = {soma}")
    elif opcao == 2:  # Caso o usuário opte pela multiplicação, utilizando a opção 2, este bloco será executado.
        multiplicar = n1 * n2
        print(f"{n1} * {n2} = {multiplicar}")
    elif opcao == 3:  # Caso o usuário opte por informar qual valor digitado é maior, utilizando a opção 3,
        # este bloco será executado.
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"Entre {n1} e {n2} o maior valor é {maior}.")
    elif opcao == 4:  # Caso o usuário opte por digitar novos valores, utilizando a opção 4, este bloco é executado.
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    else:  # Por fim, se o usuário opte pela opção 5, será encerrado o funcionamento do programa.
        print("Encerrando programa...")
        sleep(3)
        print("-=-" * 10)
        break
    print("-=-" * 10)
