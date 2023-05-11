# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 20 anos: Sênior
# - Acima: Master

from time import sleep
from datetime import date

print(f"\n{'====== DESAFIO 41 ======':^60}\n")
print(f'{"BEM VINDO(A) A CONFEDERAÇÃO NACIONAL DE NATAÇÃO!":^60}')
print(f"{'CADASTRO':^60}")

nome = input('INFORME SEU NOME: ').strip()
nascimento = int(input('INFORME O ANO EM QUE NASCEU: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

if idade <= 9:
    categoria = 'MIRIM'
elif 9 < idade <= 14:
    categoria = 'INFANTIL'
elif 14 < idade <= 19:
    categoria = 'JUNIOR'
elif 19 < idade <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f"{nome} seja bem vindo, sua categoria é a {categoria}.".upper())
