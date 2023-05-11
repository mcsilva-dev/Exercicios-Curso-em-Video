# Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e que
# se encontram no intervalor de 1 até 500.

from time import sleep

print(f"\n{'====== DESAFIO 48 ======':^82}\n")
print(f"{'NÚMEROS MULTIPLOS DE 3 E ÍMPARES DE 1 A 500':^82}\n")

soma = 0
valores = 0

for contagem in range(1, 501, 2):
    if contagem % 3 == 0:
        soma += contagem
        valores += 1
print(f"A soma de todos os {valores} números ÍMPARES e MULTIPLOS de 3 "
      f"entre 1 e 500 é igual à {soma}.")
