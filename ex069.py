"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário final quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos."""

print("\n", "DESAFIO 69".center(60), "\n")

mais_18 = homens = mulheres_20 = 0

while True:
    print("-" * 40)
    print("CADASTRE UMA PESSOA".center(40))
    print("-" * 40)
    idade = int(input("Idade: "))  # Recebe o valor da idade do usuário.
    while True:
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]  # Recebe o sexo do usuário.
        if sexo in "MF":  # Confere se é o que era esperado como resposta, caso não o laço irá continuar sendo executado
            break
    if idade >= 18:  # Verifica se a idade é maior que 18.
        mais_18 += 1  # Adiciona mais um no acumulador de idade mais_18.
    if idade < 20 and sexo == "F":
        mulheres_20 += 1
    if sexo == "M":  # Verifica se o sexo informado é MASCULINO.
        homens += 1  # Adiciona um no acumulador de homens cadastrados.
    while True:
        continuar = str(input("Quer continuar: [S/N] ")).upper().strip()[0]  # Verifica se o usuário deseja continuar.
        if continuar in 'SN':  # Se a resposta estiver dentro do esperado o laço é interrompido.
            break
    if continuar == "N":  # Checa a resposta do usuário, caso seja 'não', o laço é encerrado.
        print("===== FIM DO PROGRAMA =====".center(40))
        break
print(f"Total de pessoas com mais de 18 anos: {mais_18}")  # Informa ao usuário o total de pessoas registradas com +18.
print(f"Ao todo temos {homens} homens cadastrados.")  # Informa o número de homens cadastrados.
print(f"E temos {mulheres_20} mulher(es) com menos de 20 anos.")  # E o total de mulheres com menos de 20 anos.
