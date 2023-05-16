"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

print("\n", "DESAFIO 81".center(60), "\n")

lista = list()

while True:
    lista.append(int(input("Digite um número: ")))  # Recebe e adiciona à lista um número inteiro digitado pelo usuário.
    while True:  # Cria um looping para garantir que a resposta do usuário seja correta.
        resposta = input("Quer continuar? [S/N] ").strip().upper()[0]
        if resposta in 'SN':
            break
        else:  # Enquanto o usuário não responder corretamente será solicitado que "tente novamente".
            print("Tente novamente.", end=" ")
    if resposta == 'N':  # Caso a resposta seja "N", o looping principal é interrompido.
        lista.sort(reverse=True)  # Coloca os valores da lista em ordem decrescente.
        break

# Exibe ao usuário os resultados.
print("-" * 60)
print(f"Você digitou {len(lista)} números.")
print(f"A lista ordenada de forma decrescente é: {lista}")
print(f"O valor 5 faz parte da lista!" if 5 in lista else "O valor 5 não faz parte da lista!")
