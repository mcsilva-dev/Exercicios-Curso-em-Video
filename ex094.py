"""Crie um programa que leia nome, sexo, e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionarios em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas mulheres.
D) Uma lista com todas pessas com idade acimd da média."""

print("\n", f"{'DESAFIO 94':^58}", "\n")

lista_de_pessoas = list()
soma_idade = 0

while True:
    dados_pessoais = dict()
    dados_pessoais['Nome'] = str(input("Nome: "))
    dados_pessoais['Sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
    dados_pessoais['Idade'] = int(input("Idade: "))
    lista_de_pessoas.append(dados_pessoais.copy())
    while True:
        question = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if question in 'SN':
            break
        else:
            print("Tente novamente.", end=" ")
    if question == 'N':
        print('-' * 60)
        break

print(f"- O grupo tem {len(lista_de_pessoas)} pessoas.")

for pessoa in lista_de_pessoas:
    soma_idade += pessoa['Idade']
media = soma_idade / len(lista_de_pessoas)

print(f"- A média de idade é de {media}")
print("- As mulheres cadastras foram: ", end='')

for pessoa in lista_de_pessoas:
    if pessoa['Sexo'] == 'F':
        print(f"{pessoa['Nome']}", end=' ')

print("\n- Listas das pessoas que estão acima da média:")

for pessoa in lista_de_pessoas:
    if pessoa['Idade'] > media:
        print()
        for chave, valor in pessoa.items():
            print(f"{chave} = {valor};", end=" ")

print("\n<< ENCERRADO >>")
