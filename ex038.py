# Escreva um programa que leia dois números inteiros e compare os, mostrando na tela uma mensagem:
# - O primeiro valor é o maior
# - O segundo valor é o maior
# - Não existe valor maior, os dois são iguais.

cores = {
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'limpa': '\033[m'
}

print(f"\n{cores['verde']}{'====== DESAFIO 38 ======':^60}{cores['limpa']}\n")

pnum = int(input('Digite um número inteiro: '))
snum = int(input('Digite outro número inteiro: '))

if pnum > snum:
    print(f"O {cores['vermelho']}primeiro{cores['limpa']} valor é o {cores['verde']}maior{cores['limpa']}.")
elif pnum < snum:
    print(f"O {cores['vermelho']}segundo{cores['limpa']} valor é o {cores['verde']}maior{cores['limpa']}.")
else:
    print(f"Não existe valor maior, os dois são {cores['verde']}iguais{cores['limpa']}.")
