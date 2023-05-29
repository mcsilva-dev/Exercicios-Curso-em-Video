"""Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contando a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente."""

# MINHA PRIMEIRA SOLUÇÃO
# alunos = [[[]]]
#
# while True:
#     alunos.append(input("Nome: "))
#     alunos[0].append(float(input("Nota 1: ")))
#     alunos[0][0].append(float(input("Nota 2: ")))
#     while True:
#         question = input("Quer continuar? [S/N]").strip().upper()[0]
#         if question in "SN":
#             break
#         else:
#             print("Tente novamente.", end=" ")
#     if question == "N":
#         break
#
# print('-' * 40)
# print(f"{'No.':<10}", end="")
# print(f"{'NOME':<15}", end="")
# print(f"{'MÉDIA':<10}")
# print('-' * 40)
#
# for x in range(1, len(alunos)):
#     media = (alunos [0][x] + alunos[0][0][x - 1]) / 2
#     print(f"{x - 1:<10}", end="")
#     print(f"{alunos[x]:<15}", end="")
#     print(f"{media:<10.1f}")
#
# print('-' * 40)
#
# while True:
#     aluno = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
#     if aluno == 999:
#         print("FINALIZANDO...")
#         print("<<< VOLTE SEMPRE >>>")
#         break
#     print(f"As notas de {alunos[aluno + 1]} são [{alunos[0][aluno + 1]}, {alunos[0][0][aluno]}]")

print("\n", "DESAFIO 89".center(38), "\n")

ficha_alunos = []
aluno = []
while True:
    nome_aluno = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha_alunos.append([nome_aluno, [nota1, nota2], media])
    while True:
        continuar = input("Quer continuar [S/N] ").strip().upper()[0]
        if continuar in "SN":
            break
        else:
            print("Tente novamente.", end=" ")
    if continuar == 'N':
        break

print('-' * 40)
print(f'{"No.":<10}{"NOME":<15}{"MÉDIA":<10}')
print('-' * 40)

for indice, aluno in enumerate(ficha_alunos):
    print(f'{indice + 1:<10}{aluno[0]:<15}{aluno[2]:<10.1f}')

print('-' * 40)

while True:
    print('-' * 40)
    while True:
        aluno = int(input("Mostrar nota de qual aluno? (999 interrompe): "))
        if 0 < aluno <= len(ficha_alunos) or aluno == 999:
            break
    if aluno == 999:
        print("FINALIZANDO...")
        print("<<< VOLTE SEMPRE >>>")
        break
    print(f"As notas de {ficha_alunos[aluno - 1][0]} são {ficha_alunos[aluno - 1][1]}")
