"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000
C) Qual é o nome do produto mais barato."""

print("\n", "DESAFIO 70".center(40), "\n")
print("-" * 40)
print("LOJA SUPER BARATÃO".center(40))
print("-" * 40)
total = mais_1000 = barato = 0
nome_barato = ""  # Guarda o nome do produto mais barato.
while True:
    nome_do_produto = str(input("Nome do produto: ")).strip()  # Recebe do usuário o nome do produto.
    preco = float(input("Preço: "))  # Guarda o valor pago pelo produto.
    if barato == 0 or preco < barato:  # Checa se a variavel que guarda o valor do produto mais barato é igual a 0 ou
        # se o preco e menor que o menor preço.
        barato = preco  # Barato irá receber o valor de preço.
        nome_barato = nome_do_produto  # Nome do produto mais barato será armazenada na variavel "nome_barato".
    if preco > 1000:  # Checa se o preço foi acima de R$ 1000.
        mais_1000 += 1  # Adiciona um ao acumulador que guarda o total de produtos que custam mais de R$1000.
    total += preco  # Soma o preço do produto informado com o valor total.
    while True:
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]  # Verifica se o usuário que continuar.
        if continuar in 'SN':  # Caso o usuário informe uma das duas opções corretamente, o laço é interrompido.
            break
    if continuar == 'N':  # Se a resposta do usuário for "NÃO", o looping será encerrado.
        print(f"{'FIM DO PROGRAMA':-^40}")
        break
# Após o looping se encerrar, resume ao usuário as informações de:
# A) Total da compra.
# B) Quantidade de produtos que custaram mais de R$ 1000.
# C) O nome e valor do produto mais barato adquirido pelo usuário.
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {mais_1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {nome_barato} que custa R${barato:.2f}")
