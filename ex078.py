"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista."""

print('\n', 'DESAFIO 78'.center(50), '\n')

lista = []

while len(lista) < 5:  # Executa o looping enquanto o tamanho da lista for menor que 5.
    valor = int(input(f"Digite um valor para posição {len(lista)}: "))  # Recebe os valores do teclado do usuário.
    lista.append(valor)  # Adiciona o valor digitado pelo usuário à lista.

print("-" * 50)
print(f"Você digitou os valores {lista}")
print(f"Maior valor dentro da lista foi {max(lista)} nas posições ", end="")  # Exibe o maior valor da lista.

for indice, valor in enumerate(lista):  # Utiliza o for para exibir as posições em que o maior valor apareceu na lista.
    if valor == max(lista):  # Se o valor for o maior da lista, ele irá executar o bloco a seguir printando sua posição.
        print(indice, end="... ")

print(f"\nMenor valor dentro da lista foi {min(lista)} nas posições ", end="")  # Exibe o menor valor da lista.

for indice, valor in enumerate(lista):  # funciona da mesma forma que o bloco para exibir as posições do maior.
    if valor == min(lista):
        print(indice, end="... ")

print()
