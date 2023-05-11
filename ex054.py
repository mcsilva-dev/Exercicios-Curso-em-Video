# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas ja são maiores.

from datetime import date

print(f"\n{'====== DESAFIO 54 ======':^60}\n")

ano_atual = date.today().year
maior = 0
menor = 0

for contagem in range(1, 8):
    nascimento = int(input(f"informe a data de nascimento da {contagem} pessoa: "))
    idade = ano_atual - nascimento
    if idade < 21:
        menor += 1
    else:
        maior += 1

print('-=-' * 16)
print(f"De acordo com as datas de nascimento informadas;"
      f"\n{maior} pessoas que já atingiram a maioridade,"
      f"\ne {menor} pessoas estão abaixo.")
print('-=-' * 16)
