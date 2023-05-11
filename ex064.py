"""Crie um programa que leia vários números inteiros pelo teclado. O programa só irá para quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quandots número foram digitados e qual foi a soma entre eles
(desconsiderando o flag.)"""

print("\n", "DESAFIO 64".center(30), "\n")

total_numeros = 0  # Acumumula o total de números que for digitado pelo usuário.
soma = 0  # Soma os valores digitados pelo usuário.

while True:  # Criando um looping infinito.
    numero = int(input("Digite um número (999 para sair): "))  # Recebendo do usuário o valor de numero.
    if numero != 999:  # Caso o valor informado seja diferente do flag, este bloco será executado.
        soma += numero  # Soma o valor digitado pelo o usuário e o acumula.
        total_numeros += 1  # Acrescenta um no acumulador de numeros, cada vez que o bloco for executado.
        print(f"Você digitou {numero}.")  # Exibe na tela o número informado pelo usuário.
    else:  # Caso o usuário opte por digitar o flag, será executado o bloco, interrompendo o looping.
        print("-=-" * 20)
        break

print(f"Você digitou ao total {total_numeros} números e a soma entre eles é {soma}")  # Por fim exibi a quantidade de
# números digitados pelo usuário e a soma entre todos eles.
