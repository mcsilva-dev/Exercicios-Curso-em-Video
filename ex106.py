"""faça um mini-sistema que utilize o intecative help do Python. O usuário vai digitar um comando e o manual deve
aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores."""

print('\n', 'DESAFIO 106'.center(38), '\n')

cores = {
    'vermelho': '\033[1;31;7m',
    'verde': '\033[1;32;7m',
    'branco': '\033[1;39;7m',
    'azul': '\033[1;34;7m',
    'limpa': '\033[m'
}


def mensagem(text):
    print('~' * (len(text) + 4))
    print(text.center(len(text) + 4))
    print('~' * (len(text) + 4))


def ajuda(text):
    print(f"{cores['azul']}", end="")
    mensagem("Acessando o manual do comando '{text}'")
    print(f"{cores['limpa']}", end="")
    print(f"{cores['branco']}")
    help(text)
    print(f"{cores['limpa']}", end="")


while True:
    print(f"{cores['verde']}", end="")
    mensagem("SISTEMA DE AJUDA PyHELP")
    print(f"{cores['limpa']}", end="")
    funcao = input("Função ou Biblioteca > ").strip().lower()
    if funcao == 'fim':
        print(f"{cores['vermelho']}", end="")
        mensagem("ATE LOGO")
        print(f"{cores['limpa']}", end="")
        break
    ajuda(funcao)
