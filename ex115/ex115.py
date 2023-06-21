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
    opcoes = [0, 1, 2]
    while True:
        try:
            opcao = opcoes[int(input(F"{cores['amarelo']}Sua opção: {cores['limpa']}")) - 1]
        except (ValueError, IndexError):
            print(f"{cores['vermelho']}ERRO: Digite um número dentre as 3 opções.{cores['limpa']}")
        except KeyboardInterrupt:
            print(f"{cores['vermelho']}O usuário decidiu não informar uma opção.{cores['limpa']}")
            finalizar = True
            break
        else:
            if opcao == 0:
                funcoes.cadastradas()
                break
            elif opcao == 1:
                funcoes.cadastrar()
                break
            else:
                print('-' * 50)
                print('Saindo do sistema... Até logo!'.center(50))
                print('-' * 50)
                finalizar = True
                sleep(2)
                break
        sleep(1)
