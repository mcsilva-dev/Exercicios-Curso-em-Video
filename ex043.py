# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
# a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso.
# - Entre 18.5 e 25: Peso ideal.
# - 25 até 30: Sobrepeso.
# - 30 até 40: Obesidade.
# - Acima de 40: Obesidade mórbida.

from time import sleep
from math import pow

cores = {
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'roxo': '\033[1;35m',
    'limpa': '\033[m'
}

print(f"\n{'====== DESAFIO 43 ======':^60}\n")
print(f"{'CALCULANDO IMC':^60}\n")

altura = float(input('Informe sua altura (m): '))
peso = float(input('Informe seu peso (Kg): '))
imc = peso / pow(altura, 2)

print(f"\n{'CALCULANDO SEU IMC. AGUARDE...':^60}\n")
sleep(3)

print(f"Seu imc é de {imc:.2f}")
if imc < 18.5:
    print(f"Você está {cores['azul']}ABAIXO DO PESO{cores['limpa']}.")
elif 18.5 < imc <= 25:
    print(f"Você está com {cores['verde']}PESO IDEAL{cores['limpa']}.")
elif 25 < imc <= 30:
    print(f"Você está com {cores['amarelo']}SOBREPESO{cores['limpa']}."
          f"\nCuide melhor da sua sáude e alimentação.")
elif 30 < imc <= 40:
    print(f"Você está com {cores['roxo']}OBESIDADE{cores['limpa']}."
          f"\nCuide-se melhor, coma melhor, faça exercícios fisícos. "
          f"\nAinda há {cores['verde']}ESPERANÇA{cores['limpa']}.")
else:
    print(f"Você está com {cores['vermelho']}OBESIDADE MÓRBIDA{cores['limpa']}."
          f"\nRecomendamos que faça uma cirurgia de redução do {cores['verde']}ESTÔMAGO{cores['limpa']}."
          f"\n{cores['vermelho']}NÃO{cores['limpa']} deixe de procurar por ajuda médica "
          f"{cores['vermelho']}URGENTE{cores['limpa']}.")
