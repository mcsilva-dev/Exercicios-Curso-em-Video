"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre
o contéudo da estrutura na tela."""

print("\n", f"{'DESAFIO 90':^38}", "\n")

aluno = dict()
aluno['Nome'] = str(input("Nome: "))
aluno['Media'] = float(input(f"Média de {aluno['Nome']}: "))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for key, valor in aluno.items():
    print(f"{key} é igual a {valor}")
