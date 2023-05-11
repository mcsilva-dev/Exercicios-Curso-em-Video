"""Melhore o jogo do desafio 28 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint  # Importa a ferramente randint da biblioteca random.
from time import sleep  # Importa a ferramenta sleep da biblioteca time.

print("\n", "DESAFIO 58".center(30), "\n")
print("ADIVINHE O NÚMERO".center(30), "\n")
print("Olá, sou seu computador.")
sleep(1)  # Será utilizado sleep's para causar uma sensação de processamento e conversação entre usuário e maquina.
print("Vou pensar um número entre 0 e 10, "
      "\nseu desafio é adivinhar qual número pensei.")
sleep(3)
print("Pronto já pensei em um número, agora é com você.\n")
sleep(2)
print("Qual número eu pensei?")

valor = randint(0, 10)  # A variavel recebe um valor randomico entre 0 e 10.
palpites = 0  # Variavel para acumular o número de palpites que foram necessários para o usuário acertar.

while True:
    tentativa = int(input("Número: "))  # Recebe do usuário o número de seu palpite.
    print("Checando...")
    sleep(1)
    if tentativa != valor:  # Condição irá verificar se o valor informado pelo usuário é diferente do valor randomico
        # da variavel valor, gerado pela maquina. Caso verdadeiro o bloco é executado.
        print("hmmm, você errou! Tenta de novo.")
        if tentativa < valor:
            print("Dica: tente um número maior.")
        else:
            print("Dica: tente um número menor.")
        print("-=-" * 15)
        palpites += 1 # A cada palpite será acrescentado um a mais no número de palpites.
    else:  # Se o valor da tentativa do usuário não bater na condição anterior, significa que está correto o valor
        # informado, então é executado este bloco.
        palpites += 1
        if palpites == 1:  # Caso o usuário tenha acertado ja no primeiro palpite,
            # será exibida uma mensagem personalizada.
            print("UAU, você acertou de primeira! Parabéns!")
        else:  # Caso contrário é exibido uma mensagem comum, informando sobre seu acerto e número
            # de tentativas até acertar.
            print(f"Parabéns! você acertou com {palpites} tentativas.")
        break
