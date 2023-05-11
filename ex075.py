"""Desenvolva um programa que leia quartro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

print("\n", "DESAFIO 75".center(60), "\n")

numeros = []
while len(numeros) < 4:
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
numeros_tupla = tuple(numeros)

print('-' * 30)
print("Você digitou os números: ", end="")

for i in numeros_tupla:
    print(i, end=" ")

print(f"\nO valor 9 apareceu {numeros_tupla.count(9)} vez(es).")
if 3 in numeros_tupla:
    print(f"O valor 3 apareceu na {numeros_tupla.index(3) + 1}ª posição.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
print(f"Os valores pares digitados foram", end=" ")

for par in numeros_tupla:
    if par % 2 == 0:
        print(par, end=" ")
