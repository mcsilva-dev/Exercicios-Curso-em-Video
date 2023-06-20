"""Crie um programa que tenha uma função leiaint(), que vai funcionar, semelhante a função input() do python,
só que fazendo a validação para aceitar apenas um valor númerico."""

print('\n', 'DESAFIO 104'.center(38), '\n')
print('-' * 40)

cores = {
    'vermelho': '\033[1;31m',
    'limpa': '\033[m'
}


def leiaint(question):
    while True:
        num = input(question).strip()
        if num.isdigit():
            return int(num)
        print(f"{cores['vermelho']}ERRO! Digite um numero inteiro válido.{cores['limpa']}")


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
