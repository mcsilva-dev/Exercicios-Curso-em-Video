"""Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa
, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições."""

print("\n", "DESAFIO 101".center(38), "\n")


def idade(ano):
    from datetime import datetime as data
    atual = data.today().year
    return atual - ano


def voto(nascimento):
    pessoa_idade = idade(nascimento)
    condicoes = {
        'VOTO OBRIGATÓRIO': list(range(18, 65)),
        'VOTO OPCIONAL': list(range(16, 18)) + list(range(65, 150)),
        'NÃO VOTA': list(range(0, 18))
    }
    for key, value in condicoes.items():
        if pessoa_idade in value:
            return f'Com {pessoa_idade} anos: {key}'
    return 'Idade inválida.'


print("-" * 40)
ano_nascimento = (int(input("Em que ano você nasceu? ")))
print(voto(ano_nascimento))
