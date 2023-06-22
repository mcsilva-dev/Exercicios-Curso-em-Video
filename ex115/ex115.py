"""Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
simples.

O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas."""

import funcoes_ex115 as funcoes
from time import sleep

cores = {
    'amarelo': '\033[1;33;3m',
    'azul': '\033[1;36;3m',
    'vermelho': '\033[1;31;3m',
    'limpa': '\033[m'
}

finalizar = False

print('\n', 'DESAFIO 115'.center(38), '\n')

while not finalizar:
    print('-' * 50)
    print('MENU PRINCIPAL'.center(50))
    print('-' * 50)
    print(f"{cores['amarelo']}1{cores['limpa']} - {cores['azul']}Ver pessoas cadastradas{cores['limpa']}")
    print(f"{cores['amarelo']}2{cores['limpa']} - {cores['azul']}Cadastrar nova Pessoa{cores['limpa']}")
    print(f"{cores['amarelo']}3{cores['limpa']} - {cores['azul']}Sair do sistema{cores['limpa']}")

    while True:
        try:
            match int(input(f"{cores['amarelo']}Sua opção: {cores['limpa']}")):
                case 1:
                    funcoes.cadastradas()
                case 2:
                    funcoes.cadastrar()
                case 3:
                    print('-' * 50)
                    print('Saindo do sistema... Até logo!'.center(50))
                    print('-' * 50)
                    finalizar = True
                    break
                case _:
                    raise IndexError
        except (ValueError, IndexError):
            print(f"{cores['vermelho']}ERRO: Digite um número dentre as 3 opções.{cores['limpa']}")
        except KeyboardInterrupt:
            print(f"{cores['vermelho']}O usuário decidiu não informar uma opção.{cores['limpa']}")
            finalizar = True
            break
        except Exception as erro:
            print(f'Ocorreu um erro inesperado: {erro}')
        else:
            break
        sleep(1)
