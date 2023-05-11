"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça digitação novamente até ter um valor correto."""

print("\n", "DESAFIO 57".center(30), "\n")
print("LENDO SEXO".center(30), "\n")

while True:
    sexo = input("Informe seu sexo [M/F]: ").upper().strip()[0]  # Recebe o sexo do usuário.
    if sexo == 'M':  # Verifica se o sexo informado pelo usuário é igual a 'M', caso essa condição seja verdadeira,
        # será executado o bloco.
        print(f"Você é do sexo MASCULINO.")
        break
    elif sexo == 'F':  # Verifica se o sexo informado pelo usuário é igual a 'F', caso essa condição seja verdadeira,
        # será executado o bloco.
        print(f"Você é do sexo FEMININO.")
        break
    else:  # Caso nenhuma das condições anteriores resultar em verdadeiro, será executado o bloco adiante,
        # informando ao usuário que a opção digitada é inválida.
        print("Opção inválida! tente novamente.")
        print("-=-" * 10)
