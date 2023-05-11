# Faça um programq eu mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

from time import sleep

print(f"\n{'====== DESAFIO 46 ======':^60}\n")
print(f"{'CONTAGEM REGRESSIVA PARA ESTOURO DE FOGOS':^60}\n")

for c in range(10, -1, -1):
    print(f"{c}", end=', ') if c != 0 else print(f"{c}")
    sleep(0.5)
print(f"\033[1;32mBOOOOOOOM!\033[m")
