# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Para esse desafio irei importar a ferramenta randint da biblioteca random, para sortear o número entre 0 e 5.
from random import randint
from time import sleep
cores = {
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'limpa': '\033[m'
}

# Apresentando o titúlo do desafio e realizando a primeira interação com usuário.
print(f"\n{cores['verde']}{f'====== DESAFIO 28 ======':^60}{cores['limpa']}\n")
print(f"{cores['vermelho']}-=-{cores['limpa']}" * 20)
print(f"{'Vou pensar em um número entre 0 e 5. Tente adivinhar...':^60}")
print(f"{cores['vermelho']}-=-{cores['limpa']}" * 20)

# Realizando a randomização do valor entre 0 e 5, e recebendo o valor do usuário.
nram = randint(0, 5)
num = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(1)

# Por fim comparando o valor digita com usuário e verificando se for o mesmo valor que o sorteado.
if num == nram:
    print(f"{cores['verde']}UAU! PARABÉNS VOCÊ VENCEU!{cores['limpa']}")
else:
    print(f"{cores['vermelho']}QUE PENA, VOCÊ PERDEU! EU PENSEI NO NÚMERO {nram}, NÃO NO {num}.{cores['limpa']}")
