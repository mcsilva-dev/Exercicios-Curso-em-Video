"""Faça um programa que tenha uma função notas() que pode receber várias notas e vai retornar um dicionário com as
seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A media da turma
- A situação (opcional)
Adicione também docstrings da função."""

print('\n', 'DESAFIO 105'.center(38), '\n')
print('-' * 40)


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    notas_sala = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'media': sum(n) / len(n)
    }
    if sit:
        if notas_sala['media'] >= 7:
            notas_sala['situação'] = 'BOA'
        elif notas_sala['media'] >= 5:
            notas_sala['situação'] = 'RAZOÁVEL'
        else:
            notas_sala['situação'] = 'RUIM'
    return notas_sala


print(notas(5.5, 9.5, 10, 6.5, sit=True))
