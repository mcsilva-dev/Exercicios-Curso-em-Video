# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print(f"\n{'====== DESAFIO 52 ======':^60}\n")
print(f"{'NÚMEROS PRIMOS':^60}\n")
cores = {
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'limpa': '\033[m'
}
numero = int(input("Digite um número: "))
divisivel = 0
print(f"-=-" * 13)
for contagem in range(1, numero + 1):
    if numero % contagem == 0:  # com essa formula o laço irá checar sempre se o valor atual da contagem
        # é divisivel pelo número digitado pelo usuário, caso seja, ele irá executar esta condição.
        print(f"{cores['verde']}{contagem:^3}{cores['limpa']}", end=' ')
        divisivel += 1
    else:  # Caso o número correspondente a contagem não seja divisível pelo número informado pelo usuário,
        # será executada a excessão.
        print(f"{cores['vermelho']}{contagem:^3}{cores['limpa']}", end=' ')
    if contagem % 10 == 0:  # Solução criada para que toda vez que chegar a 10 valores exibidos, saltar uma linha.
        print()
    elif contagem == numero:  # E está solução é que para caso seja o ultimo valor do laço, também será saltada linha.
        print()
print(f"-=-" * 13)
print(f"O número {numero} foi divisível {divisivel} vezes.")
print(f"E por isso ele", end=' ')
if divisivel == 2:
    print(f"{cores['verde']}{'É PRIMO!'}{cores['limpa']}")
else:
    print(f"{cores['vermelho']}{'NÃO É PRIMO!'}{cores['limpa']}")

# Minha solução antes de assistir a resposta do professor:
# if numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0 and numero != 1:
#    print(f"O número {numero} é primo!")
# elif numero == 2 or numero == 3 or numero == 5 or numero == 7:
#    print(f"O número {numero} é primo!")
# else:
#    print(f"O número {numero} não é primo!")
