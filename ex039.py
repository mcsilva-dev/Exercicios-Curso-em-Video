# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se ja passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
from time import sleep

cores = {
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'limpa': '\033[m'
}

print(f"\n{cores['verde']}{'====== DESAFIO 39 ======':^60}{cores['limpa']}\n")
print('Olá, seja bem-vindo a junta de serviço militar!')

ano_atual = date.today().year
nome = input('Por gentileza, me informe seu nome: ')
sleep(0.5)
nascimento = int(input(f"Certo {cores['verde']}{nome}{cores['limpa']}, me informe agora o ano em que você nasceu: "))
idade = ano_atual - nascimento
sleep(1)

print(f"Aguarde por gentileza {cores['verde']}UM MOMENTO{cores['limpa']} que irei verificar suas informações...\n")
sleep(2)
print(f"{cores['verde']}-=-{cores['limpa']}" * 20, "\n")

if idade < 18:
    print(f"{cores['verde']}{nome}{cores['limpa']} sabemos que está ansioso para prestar o serviço militar,\n"
          f"porém ainda é necessário aguardar {cores['vermelho']}{18 - idade}{cores['limpa']} ano(s) para se alistar. "
          f"\nAguardamos você em {cores['verde']}{ano_atual + (18 - idade)}{cores['limpa']}, até la!")
elif idade == 18:
    print(f"{cores['verde']}{nome}{cores['limpa']} você veio na hora certa!\n"
          f"Você completou ou completará {cores['vermelho']}18{cores['limpa']} anos este ano, "
          f"então ja pode se alistar!")
else:
    print(f"{cores['verde']}{nome}{cores['limpa']} você já passou do "
          f"tempo de alistamento há {cores['vermelho']}{idade - 18} anos{cores['limpa']}."
          f"\n{cores['verde']}{nome}{cores['limpa']} você deveria ter se alistado em "
          f"{cores['vermelho']}{ano_atual - (idade - 18)}{cores['limpa']}."
          f"\n{cores['vermelho']}Aliste-se agora mesmo para prestar o serviço militar obrigatório.{cores['limpa']}")
