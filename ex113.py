"""Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
 tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""

print('\n', 'DESAFIO 113'.center(38), '\n')
print('-' * 40)

cores = {
    'vermelho': '\033[1;31m',
    'limpa': '\033[m'
}


def leiafloat(question):
    while True:
        try:
            num = float(input(question))
        except ValueError:
            print(f"{cores['vermelho']}ERRO: por favor, digite um valor real válido.{cores['limpa']}")
        except KeyboardInterrupt:
            print(f"\n{cores['vermelho']}ERRO: O usuário preferiu não digitar este número.{cores['limpa']}")
            return 0
        except Exception as erro:
            print(f"{cores['vermelho']}ERRO: {erro.__class__}.{cores['limpa']}")
        else:
            return num


def leiaint(question):
    while True:
        try:
            num = int(input(question))
        except ValueError:
            print(f"{cores['vermelho']}ERRO: por favor, digite um valor inteiro válido.{cores['limpa']}")
        except KeyboardInterrupt:
            print(f"\n{cores['vermelho']}ERRO: O usuário preferiu não digitar esse número.{cores['limpa']}")
            return 0
        except Exception as erro:
            print(f"{cores['vermelho']}ERRO: {erro.__class__}.{cores['limpa']}")
        else:
            return num


i = leiaint('Digite um número inteiro: ')
r = leiafloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {i} e o real {r}')
