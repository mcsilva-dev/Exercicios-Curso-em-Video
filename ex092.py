"""Crie um programa que leia nome, ano de nascimento, e carteira de trabalho e cadastre-os (com idade) em um dicionario
se por acaso o CPTS for diferente de ZERO, dicionário recebera também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import datetime as data

print("\n", f"{'DESAFIO 92':^38}", "\n")

ano = data.today().year
anos_contribuicao = 35

cadastro = dict()

cadastro['Nome'] = str(input("Nome: "))
cadastro['Idade'] = ano - int(input("Ano de nascimento: "))
cadastro['CTPS'] = int(input("Carteira de trabalho (0 não tem): "))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input("Ano de contratação: "))
    cadastro['Sálario'] = float(input("Salário: R$ "))
    cadastro['Aposentadoria'] = cadastro['Idade'] + (cadastro['Contratação'] + anos_contribuicao - ano)

print("-" * 40)
print(cadastro)

for chave, valor in cadastro.items():
    print(f'{chave} tem o valor {valor}')


