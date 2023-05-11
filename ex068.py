"""Faça um programa que jogue par ou ímpar. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint  # Importa a ferramenta para randomizar números da biblioteca random.

print("\n", "DESAFIO 68".center(60), "\n")
print("-=-" * 10)
print("VAMOS JOGAR PAR OU ÍMPAR".center(30))
print("-=-" * 10)
ganhou = 0  # Variavel para acumular o número de vezes que o usuário ganhou.
perdeu = False  # Variavel booleana, utilizada para checar o resultado.
while True:
    maquina = randint(0, 10)  # Randomizando um valor para o computador.
    jogador = int(input("Diga um valor: "))  # Recebendo o valor que o usuário irá jogar.
    total = jogador + maquina
    while True:
        escolha = str(input("Par ou ímpar? [P/I] ")).upper().strip()  # Recebendo a escolha do usuário.
        if escolha in 'PI':
            break
    if escolha:  # Verifica se o usuário escolheu PAR.
        if total % 2 == 0 and escolha == 'P' or total % 2 != 0 and escolha == 'I':  # Verifica se o valor do usuário
            # somado ao random da maquina é PAR.
            ganhou += 1
        else:
            perdeu = True
        print("-" * 30)
        print(f"Você jogou {jogador} e o computador {maquina}. Total de {total}", end=" ")
        print("DEU PAR" if (maquina + jogador) % 2 == 0 else "DEU ÍMPAR")
        print("Você PERDEU!" if perdeu else "Você GANHOU!\nVamos jogar novamente ...")
        print("-" * 30) if not perdeu else print(end="")
    if perdeu:  # Caso o usuário perca, será interrompido o laço
        break
print("-=-" * 10)
print(f"GAME OVER! Você venceu {ganhou} vezes." if ganhou > 1 else f"GAME OVER! Perdeu na primeita tentativa.")
