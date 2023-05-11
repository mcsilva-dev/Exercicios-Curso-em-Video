# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date

from datetime import date

print(f"\n{'====== DESAFIO 32 ======':^37}\n")

# Interação inicial com o cliente e recebimento do valor de ano.
ano = int(input('Qual ano quer analisar? (Caso queira analisar o ano atual, digite 0): '))
cores = {'Verde': '\033[1;32m',
         'Vermelho': '\033[1;31m',
         'Limpa': '\033[m'}

if ano == 0:
    ano = date.today().year
# Verificando se o ano é bissexto.
if ano % 4 == 0 and not ano % 100 == 0 or ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print(f'{ano} {cores["Verde"]}É{cores["Limpa"]} bissexto!')
else:
    print(f'{ano} {cores["Vermelho"]}NÃO É{cores["Limpa"]} bissexto!')
