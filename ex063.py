"""Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia
de fibonacci."""

print("\n", "DESAFIO 63".center(30), "\n")
print("-=-" * 10)
print("SEQUÊNCIA DE FIBONACCI".center(30))
print("-=-" * 10, "\n")

n = int(input("Informe o número de elementos: "))  # Recebe do usuário quantos elementos da sequencia de fibonacci
# ele deseja exibir na tela.
contador = 1  # Variavel contador, garante que todos elementos sejam exibidos e após isso servirá como teste logico
# para encerrar o looping e o programa.
atual = 0  # Como descrito, mantém o valor atual
anterior = atual  # Recebe o valor de atual e o armazena.
proximo = 1  # Será iniciado com 1 para que o programa funcione corretamente.
# Sua função é melhor descrita posteriormente.

print("-" * 47)
print(f"Exibindo os primeiros {n} elementos de fibonacci:")

while contador <= n:  # Enquanto o valor do contador for menor que o n, todo o bloco será executado.
    print(f"{atual} -> ", end="")
    anterior = atual  # O valor de anterior armazena o valor atual.
    atual = proximo  # O valor atual recebe o valor de proximo.
    proximo = anterior + atual  # Proximo recebe o valor anterior somado com o atual.
    contador += 1  # Sempre ao fim do bloco o contador é acrescentado o valor de 1.
print("FIM!")
