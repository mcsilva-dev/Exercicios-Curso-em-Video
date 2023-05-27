"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pessadas.
C) Uma listagem com as pessoas mais leves."""

print("\n", "DESAFIO 84".center(38), "\n")

pessoas = list()  # Guarda os dados de todas as pessoas cadastradas.
dados = list()  # Recebe os dados de cada pessoa para ser repassado a lista 'pessoas'.
maior = menor = 0  # Guardam o valor de menor e maior peso.

while True:
    dados.append(input("Nome: "))  # Recebe o nome da pessoa cadastrada e armazena na lista de dados.
    dados.append(float(input('Peso: ')))  # Recebe o peso e guarda junto ao nome na lista de dados.
    pessoas.append(dados[:])  # Copia os dados da lista 'dados' para a lista 'pessoas'.
    if len(pessoas) == 1:  # Checa se é a primeira pessoa cadastrada.
        maior = menor = dados[1]  # Se sim é atribuido o peso ao menor e maior valor.
    elif dados[1] > maior:  # É checado se o peso é maior do que o maior ja cadastrado.
        maior = dados[1]  # Caso seja o peso é substituido por um novo maior peso.
    elif dados[1] < menor:  # Aqui o mesmo que ocorre com o maior, ocorre com o menor.
        menor = dados[1]
    dados.clear()  # Limpa a lista de dados para receber os dados do próximo cadastrado.
    while True:  # Cria um looping infinito, para garantir uma resposta correta do usuário.
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]  # Recebe a resposta do usuário.
        if continuar in 'SN':  # Caso seja "S" ou "N", é interrompido o looping.
            break
        else:  # Senão é executado o bloco a seguir.
            print("Tente novamente.", end=" ")
    if continuar == 'N':  # Caso a resposta do usuário tenha sido "N" interrompe o looping principal.
        break

print('-' * 40)
print(f"Ao todo, você cadastrou {len(pessoas)} pessoas.")  # Exibe o número de pessoas cadastradas

print(f"O maior peso foi de {maior} kg. peso de ", end='')  # Exibe o maior peso.
for pessoa in pessoas:  # Cria um laço for para mostrar as pessoas que possuem o maior peso.
    if pessoa[1] == maior:
        print(f"[{pessoa[0]}]", end=" ")

print(f"\nO menor peso foi de {menor} kg. peso de ", end='')  # Exibe o menor peso.
for pessoa in pessoas:  # Ocorre o mesmo para mostrar as pessoas que possuem o maior peso.
    if pessoa[1] == menor:
        print(f"[{pessoa[0]}]", end=" ")
