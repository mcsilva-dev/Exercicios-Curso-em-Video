#  Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

from time import sleep

print(f"\n{'====== DESAFIO 47 ======':^60}\n")
for contagem in range(2, 51, 2):
    print(f"{contagem} é PAR", end=',\n') if contagem != 50 else print(f"{contagem} é PAR.")
    sleep(0.2)
print("FIM!")
