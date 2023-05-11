# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

# Interação inicial com usuário.
cores = {
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'limpa': '\033[m'
}

print(f"\n{'====== DESAFIO 29 ======':^37}\n")
print(f'Você acabou de passar por um radar que permite no máximo {cores["verde"]}80Km/h{cores["limpa"]}.')

# Verificando com usuário qual foi a velocidade que ele passou pelo radar.
vel = float(input('Em velocidade você passou por este radar? '))
radar = 80


# De acordo com a velocidade do usuário, será informado a ele caso tenha sido multado e o valor da multa.
if vel > radar:
    print(f'Você foi multado em {cores["vermelho"]}R${(vel - radar) * 7.0:.2f}{cores["limpa"]}')
print(f'Tenha um bom dia, dirija com cuidado!')
