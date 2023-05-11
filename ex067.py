"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitador for negativo."""

print("\n", "DESAFIO 67".center(60), "\n")
while True:
    numero = int(input("Quer ver a tabuada de qual valor? "))  # Recebe do usuário o número que seja ver a tabuada.
    if numero < 0:  # Se o número informado pelo usuário for negativo, o laço é encerrado.
        break
    print("-" * 35)
    for tabuada in range(1, 11):  # Realiza uma contagem de 1 até 10.
        print(f"{numero} x {tabuada} = {numero * tabuada}")  # Exibe a tabuada do número informado.
    print("-" * 35)
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")  # Informa o encerramento do programa.
