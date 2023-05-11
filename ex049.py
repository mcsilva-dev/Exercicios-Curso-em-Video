# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

from time import sleep

print(f"\n{'====== DESAFIO 49 ======':^60}\n")
print(f"{'TABUADA':^60}\n")

numero = int(input("Digite um número para ver sua tabuada: "))

print('-=-'*5)
for contagem in range(1, 11):
    tabuada = numero * contagem
    print(f"{numero} x {contagem:2} = {tabuada}")
print('-=-'*5)
