# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

print(f"\n{'====== DESAFIO 30 ======':^37}\n")

# Interação inicial com o usuário já recebendo valor de número inteiro por parte do mesmo para avaliação.
num = int(input('Digite um número inteiro: '))
cores = {
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'limpa': '\033[m'
}

# Checando se o valor é par ou ímpar de acordo com o resto da sua divisão pelo número 2.
if num % 2 == 0:
    print(f'{num} é {cores["verde"]}par{cores["limpa"]}!')
else:
    print(f'{num} é {cores["vermelho"]}ímpar{cores["limpa"]}!')
