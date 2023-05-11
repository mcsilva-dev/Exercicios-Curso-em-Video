# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# - Média abaixo de 5.0: REPROVADO.
# - Média entre 5.0 e 6.9: RECUPERAÇÃO.
# - Média 7.0 ou superior: APROVADO.

from time import sleep

cores = {
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'azul': '\033[1;34m',
    'limpa': '\033[m'
}

print(f"\n{'====== DESAFIO 40 ======':^60}\n")
print(f"{cores['vermelho']}{'-=-' * 11:^60}{cores['limpa']}")
print(f"{cores['verde']}{'AVALIAÇÃO DE DESEMPENHO ESCOLAR':^60}{cores['limpa']}")
print(f"{cores['vermelho']}{'-=-' * 11:^60}{cores['limpa']}\n")

nota1 = float(input('Digite sua primeira nota: '))
sleep(0.5)
nota2 = float(input('Digite sua segunda nota: '))
sleep(0.5)
nota3 = float(input('Digite sua terceira e ultima nota: '))
sleep(0.5)
media = (nota1 + nota2 + nota3) / 3

print("\nPROCESSANDO SEU RESULTADO FINAL. AGUARDE...\n")
sleep(3)
if media < 5:
    print(f"{cores['vermelho']}REPROVADO!{cores['limpa']}\n"
          f"Sua média foi {cores['vermelho']}{media:.2f}{cores['limpa']} e o necessário para passar é 7."
          f"\nEstude mais no próximo ano para não reprovar novamente.")
elif 5 <= media <= 6.9:
    print(f"{cores['azul']}RECUPERAÇÃO!{cores['limpa']}\n"
          f"Sua média foi {cores['azul']}{media:.2f}{cores['limpa']} e o necessário para passar é 7."
          f"\nMas você ainda tem possibilidade de ser aprovado.")
else:
    print(f"{cores['verde']}APROVADO!{cores['limpa']}\n"
          f"Sua média foi {cores['verde']}{media:.2f}{cores['limpa']}. PARABÉNS!")
