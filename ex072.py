"""Crie um programa que tenha uma tupla totalmente preenchidade com uma contagem por extenso, de 0 até 20.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso."""

print("\n", "Desafio 72".center(60), "\n")
numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze','Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        numero = int(input("Digite um número entre 0 e 20: "))
        if 0 <= numero <= 20:
            break
        print("Tente novamente.", end=" ")
    print(f"Você digitou o número {numeros[numero].lower()}.")
    while True:
        resposta = input("Quer continuar? [S/N] ").strip().upper()[0]
        if resposta in "SN":
            break
        print("Digite apenas S ou N. ", end="")
    if resposta == 'N':
        break

